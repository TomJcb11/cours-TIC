from abc import ABC, abstractmethod
import numpy as np
import pandas as pd


class BaseScaler(ABC):
    def __init__(self):
        self.numeric_column = None
        self._is_fitted = False

    @abstractmethod
    def fit(self, X: pd.DataFrame):
        pass

    @abstractmethod
    def transform(self, X: pd.DataFrame):
        pass

    def fit_transform(self, X: pd.DataFrame):
        self.fit(X)
        return self.transform(X)

    def _check_input(self, X: pd.DataFrame):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("Must be a pandas Dataframe")


class BaseEstimator(ABC):
    def __init__(self):
        self.numeric_column = None
        self._is_fitted = False

    @abstractmethod
    def fit(self, X: pd.DataFrame, y: pd.DataFrame):
        pass

    @abstractmethod
    def predict(self, X: pd.DataFrame):
        pass

    def fit_predict(self, X: pd.DataFrame, y: pd.DataFrame):
        self.fit(X, y)
        return self.predict(X)

    def _check_input(self, X: pd.DataFrame):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("Must be a pandas Dataframe")
