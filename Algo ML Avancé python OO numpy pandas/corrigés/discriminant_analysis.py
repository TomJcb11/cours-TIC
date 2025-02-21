import numpy as np
import pandas as pd
import itertools

from typing import Tuple

from base import *

class LinearDiscriminantAnalysis(Base, Estimator, Transformer):
    def __init__(self, n_components: int = None):
        self.n_components = n_components
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series) -> 'LinearDiscriminantAnalysis':
        x = self._check(x)

        self.priors, self.freq = self._get_priors(y)

        if self.n_components is not None:
            self.selected_features = self._stepdisc(x, y)
            x = x[:, self.selected_features]

        self.means, self.covariance = self._get_within_cov(x, y)
        self._inv_covariance = np.linalg.inv(self.covariance)

        self.coef = self._get_coef()
        self.intercept = self._get_intercept()

        self._fitted = True
        return self
    
    def predict(self, x: np.ndarray) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        scores = self._get_scores(x)
        return np.argmax(scores, axis=1)
    

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        self._check_fit()
        x = self._check(x)
        
        scores = self._get_scores(x)
        return self._softmax(scores)
    
    def transform(self, x: np.ndarray) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        return x[:, self.selected_features]

    def _get_priors(self, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        priors = np.bincount(y)
        return priors, priors/y.shape[0]

    def _get_within_cov(self, x: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        n_target = self.priors.shape[0]
        n_feature = x.shape[1]

        means = np.empty((n_target, n_feature))
        cov = np.empty([n_feature, n_feature, n_target])

        for t in range(n_target):
            cond = y == t
            means[t] = np.mean(x[cond], axis=0)
            cov[:, :, t] = np.cov(x[cond], rowvar=False, bias=True)
        
        return means, np.mean(cov, axis=2)
    
    def _get_coef(self) -> np.ndarray:
        return np.dot(self.means, self._inv_covariance)
    
    def _get_intercept(self) -> np.ndarray:
        return np.log(self.freq) - 0.5 * np.diag(np.linalg.multi_dot((self.means, self._inv_covariance, self.means.T)))
    
    def _get_scores(self, x: np.ndarray) -> np.ndarray:
        return np.dot(x, self.coef.T)+self.intercept
    
    def _softmax(self, scores: np.ndarray) -> np.ndarray:
        return np.exp(scores)/np.exp(scores).sum(axis=1, keepdims=True)
    
    def _stepdisc(self, x: np.ndarray, y: np.ndarray) -> Tuple[int]:
        #TODO full numpy array support ?
        _, n_features = x.shape
        unselected_features = list(range(n_features))
        
        if self.n_components >= n_features:
            return unselected_features

        w_lambda = 1
        selected_features = []
        _, wcov = self._get_within_cov(x, y)
        cov = np.cov(x, rowvar=False, bias=True)

        for component in range(self.n_components):
            for i in unselected_features:
                idx = self._get_cartesian_product(selected_features, i)

                l = self._get_w_lambda(idx, wcov, cov, component)
                if l < w_lambda:
                    w_lambda = l
                    selected_f = i

            selected_features.append(selected_f)
            unselected_features.remove(selected_f)

        selected_features.sort()
        return tuple(selected_features)

    def _get_cartesian_product(self, selected_features: list, i: int) -> Tuple[np.ndarray]:
        idx = tuple(itertools.product(selected_features+[i], selected_features+[i]))
        idx = tuple(np.transpose(idx))
        return idx

    def _get_w_lambda(self, idx: Tuple[np.ndarray], wcov: np.ndarray, cov: np.ndarray, component: int) -> float:
        return np.linalg.det(wcov[idx].reshape(-1, component+1))/np.linalg.det(cov[idx].reshape(-1, component+1))

    @property
    def n_components(self) -> int:
        return self._n_components

    @n_components.setter
    def n_components(self, n: int):
        if not isinstance(n, int):
            raise TypeError(f"Only integer object type is supported, {n.__class__.__name__} was passed")
        if n < 1:
            raise InvalidParameterError(n, (' values > 2 ',))
        self._n_components = n