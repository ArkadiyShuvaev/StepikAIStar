import numpy as np
from numpy import linalg as LA

def calculate_loss_function(X, w, y):
    product = X @ w
    subtraction_result = product - y
    result = LA.norm(subtraction_result, ord = 2)

    return result * result

# 1
# l = 2, n = 3
X = np.array([[1, 2, 3], [4, 5, 6]])
w = np.array([1, 2, 3])
y = np.array([1, 2])
print(calculate_loss_function(X, w, y)) # 1069.0000000000002

# 2
X = np.array([[1, 3, 6],[-3, 8, 1],[4, 8, 2],[-5, 1, 9]])
w = np.array([2, 5, -2])
y = np.array([3, 5, 8, 1])
print(calculate_loss_function(X, w, y)) # 2605.0000000000005
