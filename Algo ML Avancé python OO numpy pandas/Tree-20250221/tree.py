from abc import ABC, abstractmethod
from base import BaseEstimator
import random as rnd

import numpy as np



class Splitter(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def split(self, x, y):
        pass

    def check_dead_end(self, x, y):

        if(x.shape[0] == 0):
            return None
        return x, y
    

class RandomSplitter(Splitter):
    def split(self, x, y):
        record_nbr, features_nbr = x.shape

        value_idx = rnd.randrange(0, record_nbr, 1)  
        features_idx = rnd.randrange(0, features_nbr, 1)    

        value = x[value_idx, features_idx] 
        cond = x[:,features_idx] > value

        # print(value)
        # print(cond)

        # print(x[cond])
        # print(y[cond])
        # print(x[~cond])
        # print(y[~cond])

        toReturn = {
            "features": features_idx,
            "value": value,
            "left_node": self.check_dead_end( x[cond], y[cond] ),
            "right_node": self.check_dead_end( x[~cond], y[~cond] )
        }
        return toReturn


class DecisionTreeClassifier(BaseEstimator):



    def __init__(self, criterion = "Random", depth_max = None, min_samples_split = 2):
        if(criterion == "Random"): self.criterion = RandomSplitter()
        # if(criterion == "Gini"): self.criterion = GiniSplitter()
        else: raise Exception("Criterion non reconnu")

        self.depth = 0
        self.depth_max = depth_max
        self.min_samples_split = min_samples_split

        super().__init__()

    def built_tree(self, x, y):

        node = self.criterion.split(x, y)

        self.depth += 1



        if((self.depth_max is not None and self.depth > self.depth_max ) or x.shape[0] < self.min_samples_split or len(np.unique(y)) == 1):
            return  np.bincount(y).argmax()
            # return np.argmax(np.unique(y, return_counts=True))

        if(node["left_node"] is not None):
            node["left_node"] = self.built_tree(*node["left_node"]) 
        if(node["right_node"] is not None):
            node["right_node"] = self.built_tree(*node["right_node"]) 

        return node
    
    def fit(self, x, y):



        # self._check_input(x)

        self.tree = self.built_tree(x, y)

        self._is_fitted = True

        return
    
    def predict(self,x):
        predArray = np.empty(x.shape[0])

        for idx in range(0, x.shape[0]):
            prediction = self.getNextNode(self.tree, x[idx, :])
            predArray[idx] = prediction

        return predArray



    def getNextNode(self, node, x):

        if isinstance(node["left_node"], int): return node
        
        if(x[node["features"]] > node["value"]):
            # /!\ C'est le spliter qui se charge de splitter, ici on navigue !!!
            return self.getNextNode(node["left_node"], x) if isinstance(node["left_node"], dict) else node["left_node"]
        else:
            return self.getNextNode(node["right_node"], x ) if isinstance(node["right_node"], dict) else node["right_node"]



