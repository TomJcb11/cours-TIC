from abc import ABC, abstractmethod
import numpy as np
import random
from base import BaseEstimator


class Splitter(ABC):
    @abstractmethod
    def split():
        pass

    def check_dead_end(self, x, y):
        if x.shape[0] == 0:
            return
        return x, y


class RandomSplitter(Splitter):
    def split(self, x, y):
        record_nbr, feature_nbr = x.shape

        value_idx = random.randrange(0, record_nbr - 1)
        feature_idx = random.randrange(0, feature_nbr - 1)

        value = x[value_idx, feature_idx]
        cond = x[feature_idx] > value

        to_return = {
            "features": feature_idx,
            "value": value,
            "leftNode": self.check_dead_end(x[cond], y[cond]),
            "rightNode": self.check_dead_end(x[~cond], y[~cond]),
        }

        return to_return


class GiniSplitter(Splitter):
    pass


class DecisionTreeClassifier(BaseEstimator):
    def __init__(self, criterion="Random", depth_max=None, min_samples_split=2):
        if criterion == "Random":
            self.criterion = RandomSplitter()
        else:
            raise ValueError("Criterion not implemented")
        self.depth = 0
        self.depth_max = depth_max
        self.min_samples_split = min_samples_split
        self._is_fitted = False
        super().__init__()

    def build_tree(self, x, y):
        node = self.criterion.split(x, y)
        self.depth += 1
        if (
            self.depth_max is not None
            and self.depth < self.depth_max
            or x.shape[0] > self.min_samples_split
            or len(np.unique(y)) == 1
        ):
            return self.argmax(np.unique(y, return_counts=True))

        if node["leftNode"] is not None:
            self.build_tree(*node["leftNode"])

        if node["rightNode"] is not None:
            self.build_tree(*node["rightNode"])
        return

    def fit(self, x, y):
        # self._check_input(x)
        self.build_tree(x, y)
        self._is_fitted = True
        return

    def predict(self, x):
        pred_array = np.empty((x.shape[0], 1))
        for idx in range(0, x.shape[0]):
            prediction = self.get_next_node(self.tree, x[idx, :])
            pred_array[idx] = prediction
        return pred_array


def get_next_node(self, node, x):
    if x[node.features] > node.value:
        return (
            get_next_node(node.leftNode, x[node.features])
            if isinstance(node.leftNode, dict)
            else node.leftNode
        )
    else:
        return (
            get_next_node(node.rightNode, x)
            if isinstance(node.rightNode, dict)
            else node.leftNode
        )
