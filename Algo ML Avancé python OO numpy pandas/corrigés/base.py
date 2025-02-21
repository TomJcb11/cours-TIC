import numpy as np
import pandas as pd

from abc import ABC, abstractmethod

from exceptions import *

class Base(ABC):
    def __init__(self):
        self._fitted = False

    @abstractmethod
    def fit(self):
        return
    
    def _check(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        x = self._check_type(x)
        self._check_shape(x)
        return x

    def _check_type(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        if isinstance(x, np.ndarray):
            return x
        elif isinstance(x, pd.DataFrame):
            if x.iloc[:, 0].dtype == 'object':
                return np.array(x, dtype='S')
            return np.array(x)

        raise TypeError('Must be a pandas DataFrame or a numpy array')
    
    def _check_shape(self, x: np.ndarray):
        ndim = x.ndim
        if ndim != 2:
            raise DimensionError(ndim)
    
    def _check_fit(self):
        if self._fitted is False:
            raise NotFitted()


class Transformer(ABC):

    @abstractmethod
    def transform(self):
        return

    def fit_transform(self, x, y=None) -> np.ndarray:
        return self.fit(x, y).transform(x)


class Estimator(ABC):

    @abstractmethod
    def predict(self):
        return

    def fit_predict(self):
        return self.fit().predict()


class Splitter(ABC):
    @abstractmethod
    def _split(self, x, y):
        return

    def __call__(self, x: np.array, y: np.array) -> dict:
        return self._split(x, y)
    
    def _check_dead_end(self, x: np.array, y: np.array) -> None | tuple:
        if y.shape[0] == 0:
            return
        return x, y