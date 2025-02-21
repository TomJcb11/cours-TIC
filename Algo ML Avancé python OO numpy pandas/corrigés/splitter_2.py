from base import Splitter

import numpy as np
from typing import Tuple

EPS = np.finfo(np.float64).eps

class RandomSplitter(Splitter):
    def __init__(self):
        super().__init__()

    def _split(self, x: np.ndarray, y: np.ndarray) -> dict:
        n_sample, n_feature = x.shape
        idx = (np.random.randint(0, n_sample), np.random.randint(0, n_feature))

        feature = idx[1]
        value = x[idx]
        condition = x[:, feature] < value

        return {
            'feature': feature,
            'value': value,
            'left': self._check_dead_end(x[condition], y[condition]),
            'right': self._check_dead_end(x[~condition], y[~condition])
        }


class GiniSplitter(Splitter):
    def __init__(self):
        super().__init__()

    def _split(self, x: np.ndarray, y: np.ndarray) -> dict:
        _, n_feature = x.shape
        best_gini = 10

        for feature in range(n_feature):
            for value in np.unique(x[:, feature]):
                condition = x[:, feature] < value
                gini = self._get_w_gini(y[condition], y[~condition])

                if gini < best_gini:
                    best_gini = gini
                    best_value = value
                    best_feature = feature

        condition = x[:, best_feature] < best_value

        return {
            'feature': best_feature,
            'value': best_value,
            'gini': best_gini,
            'left': self._check_dead_end(x[condition], y[condition]),
            'right': self._check_dead_end(x[~condition], y[~condition])
        }

    def _get_w_gini(self, *leaves: tuple) -> float:
        ginis = np.empty(2)
        count = np.empty(2)

        for idx, leaf in enumerate(leaves):
            ginis[idx], count[idx] = self._get_gini(leaf)

        return np.average(ginis, weights=count)

    def _get_gini(self, leaf: np.array) -> Tuple[float, int]:
        unique = self._unique(leaf, False)
        n_sample = unique.sum()
        freq = unique/n_sample
        gini = 1-np.sum(freq*freq)
        return gini, n_sample
    
    def _unique(self, leaf: np.array, zero: bool = True) -> np.array:
        unique = np.bincount(leaf)
        return unique if zero else unique[unique != 0]


class EntropySplitter(Splitter):
    def __init__(self) -> None:
        super().__init__()

    def _split(self, x: np.ndarray, y: np.ndarray) -> dict:
        _, n_feature = x.shape
        best_entropy = -np.log(EPS)

        for feature in range(n_feature):
            for value in np.unique(x[:, feature]):
                condition = x[:, feature] < value
                entropy = self._get_w_entropy(y[condition], y[~condition])

                if entropy < best_entropy:
                    best_entropy = entropy
                    best_value = value
                    best_feature = feature

        condition = x[:, best_feature] < best_value

        return {
            'feature': best_feature,
            'value': best_value,
            'entropy': best_entropy,
            'left': self._check_dead_end(x[condition], y[condition]),
            'right': self._check_dead_end(x[~condition], y[~condition])
        }
    
    def _get_w_entropy(self, *leaves: tuple) -> float:
        entropies = np.empty(2)
        count = np.empty(2)

        for idx, leaf in enumerate(leaves):
            entropies[idx], count[idx] = self._get_entropy(leaf)

        return np.average(entropies, weights=count)
         
    def _get_entropy(self, leaf: np.array) -> Tuple[float, int]:
        n_sample = self._unique(leaf, False)
        freq = n_sample/n_sample.sum()
        entropy = -np.sum((freq*np.log(freq)))

        return entropy, n_sample.sum()
    
    def _unique(self, leaf: np.array, zero: bool = True) -> np.array:
        unique = np.bincount(leaf)
        return unique if zero else unique[unique != 0]