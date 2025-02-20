import pandas as pd 
import numpy as np

class MinMaxScalerHM :

    def __init__(self):

        self.mini = None
        self.maxi = None
        self.numeric_column = None
    
    def fit(self, X : pd.DataFrame):

        self.numeric_column = X.select_dtypes(np.number).columns

        self.mini = X[self.numeric_column].min()
        self.maxi = X[self.numeric_column].max()

    def transform(self, X : pd.DataFrame): 

        X_scaled = X.copy()

        X_scaled[self.numeric_column] = (X[self.numeric_column] - self.mini) / (self.maxi - self.mini)

        return X_scaled