# Exercise: https://stepik.org/lesson/819422/step/5?unit=822810

import numpy as np
from numpy import linalg as LA

def solve_linear_regression(X: np.ndarray, y):
    product = X.T @ X
    inv = LA.inv(product)
    c = inv @ X.T
    w_opt = c @ y

    return w_opt


X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([1, 1, 1])
print(solve_linear_regression(X, y))
