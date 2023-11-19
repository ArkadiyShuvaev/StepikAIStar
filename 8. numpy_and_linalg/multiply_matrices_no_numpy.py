import numpy as np
import random
import scipy.stats as sps

def no_numpy_mult(a, b):
    """
    A: list of "size" lists, each contains "size" floats --- первая матрица-аргумент
    B: list of "size" lists, each contains "size" floats --- вторая матрица-аргумент
    return C: list of "size" lists, each contains "size" floats --- матрица, являющаяся результатом умножения матриц a и b

    Функция принимает на вход две матрицы: A и B размерностью size x size
    Возвращает матрицу их произведения A * B = C

    Реализуйте умножение матриц без использования функций из пакета numpy
    """
    result = np.array([a.shape[0], b.shape[1]])
    print(result)

    def ensure_size(a, b):
      if (a.ndim != b.ndim):
        raise Exception("ndim")

      if (a.shape[0] != b.shape[1]):
        raise Exception("shape")

    def calculate_column(a, b, column_b_idx):
      result = np.empty(a.shape[0])
      for row_idx_in_a in range(a.shape[0]):
        for item_idx_in_column_b in range(b.shape[1]):


    # def multiply_matrices(a, b):
    #   for column_idx_in_b in range(b.shape[1]):
    #     col = calculate_column(a, b, column_idx_in_b)
    #     result[column_b_idx] = col



    ensure_size(a, b)
    return a

no_numpy_mult(a, b)
