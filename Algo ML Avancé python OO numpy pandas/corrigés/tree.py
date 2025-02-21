import numpy as np
import pandas as pd

from base import Base, Estimator, Transformer
from splitter import *
from exceptions import InvalidParameterError

SPLITTERS = {
    'random': RandomSplitter,
    'gini': GiniSplitter,
    'entropy': EntropySplitter
}


class DecisionTreeClassifier(Base, Estimator):
    def __init__(self, criterion: str = 'gini', max_depth: int = 10, min_sample_split: int = 2):
        self.max_depth = max_depth
        self.criterion = criterion
        self.min_sample_split = min_sample_split
        super().__init__()

    def fit(self, x: np.ndarray | pd.DataFrame, y: np.ndarray | pd.Series) -> 'DecisionTreeClassifier':
        x = self._check(x)
        self._splitter = SPLITTERS[self.criterion]()
        self.tree = self._build_tree(x, y)

        self._fitted = True
        return self
    
    def predict(self, x: np.ndarray | pd.DataFrame) -> np.ndarray:
        self._check_fit()
        x = self._check(x)

        y_pred = np.empty(x.shape[0], dtype=np.int32)

        for idx, sample in enumerate(x):
            y_pred[idx] = self._get_next_node(sample, self.tree)
        return y_pred

    def _build_tree(self, x: np.ndarray, y: np.ndarray, depth: int = 0) -> dict|int:
        n_samples, _ = x.shape
        unique = self._unique(y)
        if depth == self.max_depth or n_samples < self.min_sample_split or unique[unique != 0].shape[0] == 1:
            return np.argmax(unique)
        
        split = self._splitter(x, y)

        node = {
            'feature': split.get('feature'),
            'value': split.get('value'),
            self.criterion: split.get(self.criterion),
            'depth': depth
            }
        
        depth += 1

        if split.get('left') is not None:
            node['left'] = self._build_tree(*split.get('left'), depth=depth)

        if split.get('right') is not None:
            node['right']  = self._build_tree(*split.get('right'), depth=depth) 

        return node
    
    def _get_next_node(self, x: np.ndarray, node: dict) -> int:
        feature = node.get('feature')
        value = node.get('value')
        left = node.get('left')
        right = node.get('right')

        if (x[feature] < value) and left is not None:
            return self._get_next_node(x, left) if isinstance(left, dict) else left
        else:
            return self._get_next_node(x, right) if isinstance(right, dict) else right
        
    def _unique(self, leaf: np.ndarray, zero: bool = True) -> np.ndarray:
        unique = np.bincount(leaf)
        return unique if zero else unique[unique != 0]

    @property
    def criterion(self) -> str:
        return self._criterion
    
    @criterion.setter
    def criterion(self, crit: str):
        if crit not in SPLITTERS.keys():
            raise InvalidParameterError(crit, SPLITTERS.keys())
        self._criterion = crit

    @property
    def min_sample_split(self) -> str:
        return self._min_sample_split
    
    @min_sample_split.setter
    def min_sample_split(self, min: int):
        if not isinstance(min, int):
            raise TypeError(f"Only integer object type is supported, {min.__class__.__name__} was passed")
        if min < 2:
            raise InvalidParameterError(min, (' values > 2 ',))
        self._min_sample_split = min

    def __repr__(self) -> str:
        return 'DecisionTreeClassifier'
