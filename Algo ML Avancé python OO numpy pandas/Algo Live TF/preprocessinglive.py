import pandas as pd 
import numpy as np 
from base import BaseScaler





class MinMaxScalerHM(BaseScaler):

    def __init__(self, range : tuple[int,int] =(0,1)):

        super().__init__()
        self.range = range
        self.mini = None
        self.maxi = None
        self.column_name = None

    
    def fit(self, X : pd.DataFrame ):

        self._check_input(X)

        self.numeric_column = X.select_dtypes(np.number).columns

        self.mini = X[self.numeric_column].min()
        self.maxi = X[self.numeric_column].max()

        self._is_fitted = True

    def transform(self, X : pd.DataFrame | np.ndarray):

        if not self._is_fitted :
            raise ValueError('Model not fitted')

        X_scaled = X.copy()

        X_scaled[self.numeric_column] = (((X_scaled[self.numeric_column] - self.mini) / (self.maxi - self.mini)) * (self.range[1] - self.range[0])) + self.range[0] 

        return X_scaled
    


    


class RobustScalerHM(BaseScaler): 

    def __init__(self):
        
        super().__init__()
        self.median = None
        self.iqr = None
        self.Q1 = None
        self.Q3 = None

    def fit(self, X : pd.DataFrame) :

        self._check_input(X)

        self.numeric_column = X.select_dtypes(np.number).columns

        self.Q1 = X[self.numeric_column].quantile(axis=0,q=0.25)
        self.Q3 = X[self.numeric_column].quantile(axis=0,q=0.75)

        self.median = X[self.numeric_column].median(axis=0)
        self.iqr = self.Q3 - self.Q1

        self._is_fitted = True
    
    def transform(self, X : pd.DataFrame ):

        if not self._is_fitted:
            
            raise ValueError('Model Not Fitted')

        X_scaled = X.copy()

        # Todo retravailler cette partie pour une meilleur gestion de la division par 0

        if sum(self.Q1) == sum(self.Q3):

            X_scaled[self.numeric_column] = 0
        
        else :

            X_scaled[self.numeric_column] = (X_scaled[self.numeric_column] - self.median) / self.iqr 

        return X_scaled
    




class StandardScalerHM(BaseScaler) :

    def __init__(self):

        super().__init__()
        self.mean = None
        self.std = None

    def fit(self, X : pd.DataFrame):

        self._check_input(X)

        self.numeric_column = X.select_dtypes(np.number).columns

        self.mean = X[self.numeric_column].mean(axis=0)
        self.std = X[self.numeric_column].std(axis=0,ddof=0)

        self._is_fitted = True

    def transform(self, X : pd.DataFrame):

        if not self._is_fitted :

            raise ValueError('Model Not Fitted')

        X_scaled = X.copy()

        X_scaled[self.numeric_column] = (X_scaled[self.numeric_column] - self.mean) / self.std

        return X_scaled
     



class MyOneHotEncoder :
 
    def __init__(self, drop_first = True):
        self.drop_first = True
        self.object_columns = None
        self._isfit = False
   
    def fit(self, X : pd.DataFrame):
        self.object_columns = X.select_dtypes(object).columns
        self.uniques = dict()
        for col in self.object_columns:
            unique = X[col].unique()
            if len(unique) < 10:
                unique = sorted(unique)
                self.uniques[col] = unique
        self._isfit = True
 
    def transform(self, X : pd.DataFrame):
        if not self._isfit: raise Exception('fit() not called before')
        X_scaled = X.copy()
        for col in self.uniques:
            for index, new_col in enumerate(self.uniques[col]):
                if index != 0 or not self.drop_first:
                    X_scaled[new_col] = X_scaled[col] == new_col
        return X_scaled
   
    def fit_transform(self, X : pd.DataFrame):
        self.fit(X)
        return self.transform(X)
    

class OneHotEncoderHM:

    def __init__(self):

        self.categorical_column = None

    def fit(self,X : pd.DataFrame):

        self.categorical_column = X.select_dtypes("object").columns

    def transform(self,X : pd.DataFrame):

        X_scaled = X.copy()

        for col in self.categorical_column :
            new_col = X_scaled[col].unique()
            for feature in new_col:
                X_scaled[feature] = X_scaled[col] == feature
                
        return X_scaled

    def fit_transform(self,X ):
        self.fit(X)
        return self.transform(X)
    



class OrdinalEncoderHM:

    def __init__(self, values : list[str] = None):

        self.values = values

    def fit(self, X : pd.Series):

        if self.values == None:
             self.values = list(X.unique())
        else:
            for i in range(len(X)):
                if X[i] not in self.values:
                    raise ValueError('Value not in given list :', X[i])

    def transform(self, X : pd.Series):

        X_scaled = np.zeros(len(X))
        
        for i in range(len(X)):
            X_scaled[i] = self.values.index(X[i])

        return X_scaled
    
    def fit_transform(self, X : pd.Series):

        self.fit(X)

        return self.transform(X)
    



class MyOrdinalEncoder :
   
    def __init__(self, categories = None):
        self.categories = categories
        self.object_columns = None
        self._isfit = False
   
    def fit(self, X : pd.DataFrame):
        self.object_columns = X.select_dtypes(object).columns
        self.uniques = dict()
        for col in self.object_columns:
            unique = X[col].unique()
            if len(unique) < 100:
                unique = sorted(unique)
                if self.categories :
                    for lc in self.categories:
                        if len(lc) == len(unique):
                            ok = True
                            for lci in lc:
                                print(lci)
                                if lci not in unique:
                                    ok = False
                                    break
                            if ok:
                                unique = lc
                                break
                    self.uniques[col] = unique
        self._isfit = True
 
    def transform(self, X : pd.DataFrame):
        if not self._isfit: raise Exception('fit() not called before')
        X_scaled = X.copy()
        for col in self.uniques:
            for index, new_col in enumerate(self.uniques[col]):
                X_scaled[col] = X_scaled[col].replace(to_replace=new_col, value=str(index))
            X_scaled[col] = X_scaled[col].astype(np.float32)
        return X_scaled
   
    def fit_transform(self, X : pd.DataFrame):
        self.fit(X)
        return self.transform(X)
    

 
class OrdinalEncoderHMS:
    def __init__(self):
       
        self.categories_ = None
        self.ordered_categories_ = None
 
    def fit(self, X: pd.DataFrame):
       
        self.categories_ = {}
        self.ordered_categories_ = {}
        for col in X.columns:
            self.categories_[col] = sorted(X[col].dropna().unique())
            self.ordered_categories_[col] = {category: index for index, category in enumerate(self.categories_[col])}
        return self
   
    def transform(self, X: pd.DataFrame):
       
        X_encoded = X.copy()
        for col in X.columns:
            X_encoded[col] = X[col].map(self.ordered_categories_[col])
        return X_encoded
   
    def fit_transform(self, X: pd.DataFrame):
   
        self.fit(X)
        return self.transform(X)