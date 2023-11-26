import numpy as np

# pure Python
def no_numpy_mult(a, b):
    """
    A: list of "size" lists, each contains "size" floats. The size is N x M.
    B: list of "size" lists, each contains "size" floats. The size is M x K.
    return C: list of "size" lists, each contains "size" floats. The result size is N x K.
    """

    def ensure_size(a, b):
      if (len(a[0]) != len(b)):
        raise Exception("size")

    def multiply_matrices(a, b) -> list[list[float]]:
      result = [[0.0 for _ in range(len(b[0]))] for _ in range(len(a))]

      for i in range(len(result)):
        for j in range(len(result[0])):
          for m in range(len(a[0])):
            result[i][j] += a[i][m] * b[m][j]

      return result

    ensure_size(a, b)
    result = multiply_matrices(a, b)

    return result

def numpy_mult(first, second):
    """
    A: np.array[size, size]              --- первая матрица-аргумент
    B: np.array[size, size]              --- вторая матрица-аргумент
    return C: np.array[size, size]       --- матрица, являющаяся результатом умножения матриц A и B

    Функция принимает на вход две матрицы: A и B размерностью size x size
    Возвращает матрицу их произведения A * B = C

    Реализуйте умножение матриц, используя функции из пакета numpy    """

    return first @ second

def no_numpy_mult_2(a, b):
    """
    A: list of "size" lists, each contains "size" floats --- первая матрица-аргумент
    B: list of "size" lists, each contains "size" floats --- вторая матрица-аргумент
    return C: list of "size" lists, each contains "size" floats --- матрица, являющаяся результатом умножения матриц a и b

    Функция принимает на вход две матрицы: A и B размерностью size x size
    Возвращает матрицу их произведения A * B = C

    Реализуйте умножение матриц без использования функций из пакета numpy
    """

    def ensure_size(a, b):
      if (a.ndim != b.ndim):
        raise Exception("ndim")

      if (a.shape[1] != b.shape[0]):
        raise Exception("shape")

    def calculate_column(a, b, column_idx_of_b):
      column_values_of_b = b[:, column_idx_of_b]
      calculation_result = np.zeros(a.shape[0])
      for row_idx_of_a in range(a.shape[0]):
        for column_value_idx in range(len(column_values_of_b)):
          # multiply columns of matrix "a" by the column of matrix "b"
          calculation_result[row_idx_of_a] += a[row_idx_of_a, column_value_idx] * column_values_of_b[column_value_idx]

      return calculation_result

    def set_result(result_matrix, column_index, column_values):
      for idx in range(result_matrix.shape[0]):
        result_matrix[idx, column_index] = column_values[idx]

    def multiply_matrices(a, b):
      result = np.empty([a.shape[0], b.shape[1]])

      for column_idx_of_b in range(b.shape[1]):
        col = calculate_column(a, b, column_idx_of_b)
        set_result(result, column_idx_of_b, col)

      return result

    ensure_size(a, b)
    result = multiply_matrices(a, b)

    return result


# a = np.random.sample((2, 5))
# b = np.random.sample((5, 3))
arr_a = [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]
arr_b = [[0, 5, 1], [1, 6, 2], [2, 7, 3], [3, 8, 4], [4, 0, 5]]
a = np.array(arr_a, dtype = float)
b = np.array(arr_b, dtype = float)

print(no_numpy_mult(arr_a, arr_b))
print(numpy_mult(a, b))
