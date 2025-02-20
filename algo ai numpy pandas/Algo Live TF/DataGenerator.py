import pandas as pd
import numpy as np


class Generate_Data():

    """ Class pour générer des données a des fins de test.
    nan : Bool to activate nan value in the dataset Default = False
    pctnan : Float between 0. and 1. % of nan values Default = 0
    size : Int number of sample Default = 10
    target : Bool Add a target column, values [0,1,2] Default = False
    """

    def __init__(self):

        self.education_levels = ["Primaire", "Secondaire", "Licence", "Master"]

    def get_data(self,nan=False,pctnan=0.0,size=10,target=False):

        df = pd.DataFrame({
        "Age": np.random.randint(20, 60, size=size).astype(float),
        "Salaire": np.random.randint(25000, 80000, size=size).astype(float),
        "Heures_travail": np.random.randint(20, 60, size=size).astype(float),
        "Ville": np.random.choice(["Paris", "Lyon", "Marseille", "Bordeaux", "Nantes"], size=size),
        "Éducation": np.random.choice(self.education_levels, size=size)
        })
        if target:
            df = pd.concat((df,pd.Series(data=np.random.randint(0,3,size),name='Target')),axis=1)
        if nan :
            for col in ["Age", "Salaire", "Heures_travail", "Ville", "Éducation"]:
                df.loc[df.sample(frac=pctnan).index, col] = np.nan
        return df