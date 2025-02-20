import numpy as np
import pandas as pd
from functools import partial

from base import *
from exceptions import *

from typing import Tuple


class OrdinalEncoder(Base, Transformer):
    # TODO ADD support for unknown value
    """
    Encode categorical features.
    An integer is assigned to each discrete unique value for each feature.
    Return a array of ordinal integers from 0 to n_category-1 for each feature.
    Categories are sorted before assigning an integer.

    Ordinal encoder should only be used for ordinal features, please 
    refer to OneHotEncoder for non ordinal features. 

    Examples:
    >>> from preprocessing import OrdinalEncoder
    >>> encoder = OrdinalEncoder()
    >>> x = pd.DataFrame({
        'x1': ['green', 'green', 'yellow', 'red', 'yellow'],
        'x2': ['banana', 'apple', 'apple', 'orange', 'apple']})
    >>> encoder.fit_transform(x)
        [[0 1]
        [0 0]
        [2 0]
        [1 2]
        [2 0]]

    """
    def __init__(self) -> 'OrdinalEncoder':
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series = None) -> 'OrdinalEncoder':
        """
        For each feature, retrieve unique values and assign a integer.

        Args:
            x (np.ndarray | pd.DataFrame): 2D array like input features.
            y (np.ndarray | pd.Series, optional): 1D array like. Only present for pipeline 
            compatibility. Defaults to None.

        Returns:
            OrdinalEncoder: fitted OrdinalEncoder class object
        """
        x = self._check(x)

        _, self.n_features = x.shape
        self.encoder = {}

        for idx in range(self.n_features):
            cat = np.unique(x[:, idx])
            self.encoder[idx] = dict(zip(cat, np.arange(0, cat.shape[0])))

        self._fitted = True
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        """
        Map each category of each feature with corresponding integer.

        Args:
            x (np.ndarray): input feature. Input shape must have the same 
            number of column as seen during fitting.

        Raises:
            ShapeMissmatch: different number of a column than previously 
            seen during fitting

        Returns:
            np.ndarray: encoded features
        """
        self._check_fit()
        x = self._check(x)

        n_samples, n_features = x.shape
        if n_features != self.n_features:
            raise ShapeMissmatch(self.n_features, n_features)
        
        x_enc = np.empty((n_samples, n_features), dtype=int)
        for idx, map in self.encoder.items():
            x_enc[:, idx] = np.select([x[:, idx] == cat for cat in map], map.values())

        return x_enc

    def __repr__(self) -> str:
        return 'OrdinalEncoder'


class StandardScaler(Base, Transformer):
    #TODO add support for only centering
    """
    Standardize features by centering reducing process. After transformation 
    each feature will have a mean of 0 and an variance of 1.

    The mean and the standard deviation are computed on the trainset and then stored.
    Any further data will be standardize with the stored values.

    This is as common requirement for many algorithms and they may behave 
    inconsistently with non standardized data(e.g. SVM).

    A contrario, some algorithms does not require any standardization
    (e.g. decision trees).

    Examples:
    >>> from preprocessing import StandardScaler
    >>> x = np.random.randint(0, 10, (10, 5))
    >>> enc = StandardScaler()
    >>> x_enc = enc.fit_transform(x)
    >>> print(x_enc.mean(axis=0), x_enc.std(axis=0))
    [ 6.66133815e-17 -1.55431223e-16  6.66133815e-17  0.00000000e+00
    1.33226763e-16] [1. 1. 1. 1. 1.]


    """
    def __init__(self) -> 'StandardScaler':
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series = None) -> 'StandardScaler':
        """
        Compute and stored mean and standard deviation for each input feature.

        Args:
            x (np.ndarray | pd.DataFrame): 2D array like input features.
            y (np.ndarray | pd.Series, optional): Only presents for pipeline 
            compatibility. Defaults to None.

        Returns:
            StandardScaler: fitted StandardScaler class object
        """
        x = self._check(x)

        self.mean = x.mean(axis=0)
        self.std = x.std(axis=0)

        self._fitted = True
        return self

    def transform(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        """
        standardize each feature by removing the mean and dividing by the 
        standard deviation

        Args:
            x (np.ndarray): input feature. Input shape must have the same 
            number of column as seen during fitting.

        Returns:
            np.ndarray: standardized feature
        """
        self._check_fit()
        x = self._check(x)

        return (x-self.mean)/self.std

    def __repr__(self) -> str:
        return 'StandardScaler'


class OneHotEncoder(Base, Transformer):
    """
    Create a binary column for each unique category.

    It does not create an order contray to Ordinal Encoder.

    Examples:
    >>> from preprocessing import OneHotEncoder
    >>> enc = OneHotEncoder()
    >>> x = np.array([['dark', 'jean'], ['yellow', 'shirt'], ['red', 'tshirt']]) 
    >>> enc.fit_transform(x)
    array([[1., 0., 0., 1., 0., 0.],
        [0., 0., 1., 0., 1., 0.],
        [0., 1., 0., 0., 0., 1.]])

    """
    def __init__(self, keep_last: bool = True):
        """

        Args:
            keep_last (bool, optional): For each feature keep all categories or n-1 to eliminate
            redundancy. Defaults to True.
        """
        self.keep_last = keep_last
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series = None) -> 'OneHotEncoder':
        """
        Retrieve unique categories for all features. 

        Args:
            x (np.ndarray | pd.DataFrame): _description_
            y (np.ndarray | pd.Series, optional): _description_. Defaults to None.

        Returns:
            OneHotEncoder: _description_
        """
        x = self._check(x)

        _, self.n_features = x.shape
        self.encoder = {}
        self.n_cat = 0

        for idx in range(self.n_features):
            categories = np.unique(x[:, idx])

            if not self.keep_last:
                categories = categories[:categories.shape[0]-1]

            [self.encoder.update({i+self.n_cat: (cat, idx)}) for i, cat in enumerate(categories)]
            self.n_cat += categories.shape[0]

        self._fitted = True
        return self

    def transform(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        x_enc = np.zeros((x.shape[0], self.n_cat))

        for idx, (cat, col) in self.encoder.items():
            x_enc[x[:, col] == cat, idx] = 1

        return x_enc

    @property
    def keep_last(self) -> bool:
        return self._keep_last

    @keep_last.setter
    def keep_last(self, keep_last):
        if not isinstance(keep_last, bool):
            raise TypeError(
                f'Must be a boolean object type not {keep_last.__class__.__name__}')

        self._keep_last = keep_last

    def __repr__(self) -> str:
        return 'OneHotEncoder'


class SimpleImputer(Base, Transformer):
    def __init__(self, strategy: str):
        self.strategy = strategy
        self._imputers = {
            'mean': np.nanmean,
            'median': partial(np.nanquantile, q=0.5),
            'most_frequent': partial(np.unique, return_counts=True)
        }
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series = None) -> 'SimpleImputer':
        x = self._check(x)
        _, self.n_features = x.shape

        self.encoder = {}
        for idx in range(self.n_features):
            self.encoder[idx] = self._get_value(x[:, idx])

        self._fitted = True
        return self

    def transform(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        for idx, value in self.encoder.items():
            if x.dtype.type is np.string_:
                x[x[:, idx] == 'nan', idx] = value
            else:
                x[np.isnan(x[:, idx]), idx] = value

        return x

    def _get_value(self, x: np.ndarray) -> int | str:
        func = self._imputers.get(self.strategy)
        if self._strategy == 'most_frequent':
            cat, count = func(x)
            return cat[np.argmax(count)]
        return func(x)

    @property
    def strategy(self) -> str:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: str):
        if strategy not in self._imputers.keys():
            raise InvalidParameterError(strategy, self._imputers.keys())
        self._strategy = strategy

    def __repr__(self) -> str:
        return 'SimpleImputer'

   
class OutlierDetector(Base, Estimator):
    def __init__(self, method='tukey'):
        self._methods = ('tukey',)
        self.method = method
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series = None) -> 'OutlierDetector':
        x = self._check(x)
        _ , self.n_features = x.shape

        self.bounds = {}

        for idx in range(self.n_features):
            self.bounds[idx] = self._get_bounds(x[:, idx])

        self._fitted = True
        return self
    
    def predict(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        n_samples, _ = x.shape
        outlier_mask = np.full((n_samples, self.n_features), False)

        for idx, (lower, upper) in self.bounds.items():
            outlier_mask[:, idx] = (x[:, idx] < lower) | (x[:, idx] > upper)

        return np.any(outlier_mask, axis=1)

    def _get_bounds(self, x: np.ndarray) -> Tuple[float, float]:
        q1 = np.quantile(x, .25)
        q3 = np.quantile(x, .75)
        iqr = (q3-q1)*1.5

        return q1-iqr, q3+iqr

    @property
    def method(self) -> str:
        return self._method
    
    @method.setter
    def method(self, method: str):
        if method not in self._methods:
            raise InvalidParameterError(method, self._methods)
        self._method = method

    def __repr__(self) -> str:
        return 'OutlierDetector'
