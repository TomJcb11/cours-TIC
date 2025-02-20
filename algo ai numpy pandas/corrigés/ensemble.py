import numpy as np
import pandas as pd

from base import Base, Estimator
from exceptions import *
from tree import DecisionTreeClassifier

from typing import Tuple


class RandomForestClassifier(Base, Estimator):
    def __init__(self, n_estimators: int = 20, criterion: str = 'gini', max_depth: int = 20, min_sample_split: int = 2):
        self.n_estimators = n_estimators
        self._base_estimator = DecisionTreeClassifier
        self._base_estimator_params = {
            'criterion': criterion,
            'max_depth': max_depth,
            'min_sample_split': min_sample_split
        }
        
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series) -> 'RandomForestClassifier':
        x = self._check(x)
        self._trees = list(self._build_forest(x, y))

        self._fitted = True
        return self
    
    def predict(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        n_sample, _ = x.shape
        y_pred = np.empty(n_sample, dtype=np.int32)

        for idx, _ in enumerate(x):
            y_pred[idx] = self._get_prediction(x[idx:idx+1, :])

        return y_pred
    
    def _build_forest(self, x: np.ndarray, y: np.ndarray):
        for _ in range(self.n_estimators):
            x_resampled, y_resampled = self._get_bootstrap(x, y)
            tree = self._base_estimator(**self._base_estimator_params)
            tree.fit(x_resampled, y_resampled)
            yield tree
    
    def _get_bootstrap(self, x: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        n_sample, _ = x.shape
        idx = np.random.randint(0, n_sample, size=n_sample)
        return x[idx], y[idx]
    
    def _get_prediction(self, x: np.ndarray) -> int:
       return np.argmax(np.bincount([tree.predict(x)[0] for tree in self._trees]))
    
    @property
    def n_estimators(self) -> int:
        return self._n_estimators
    
    @n_estimators.setter
    def n_estimators(self, n_estimators: int):
        if n_estimators < 2:
            raise InvalidParameterError(n_estimators, ('> 2',))
        self._n_estimators = n_estimators
    
    def __repr__(self) -> str:
        return 'RandomForestClassifier'