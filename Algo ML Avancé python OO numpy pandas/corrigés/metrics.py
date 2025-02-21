import numpy as np

def accuracy(y_true: np.array, y_pred: np.array) -> float:
    return np.sum(y_true == y_pred)/y_true.shape[0]