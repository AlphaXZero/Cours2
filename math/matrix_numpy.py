import numpy as np
from tabulate import tabulate
from random import randint
import time


def generate_matrix(rowcol: tuple[int, int]) -> np.ndarray:
    return np.random.randint(1, 21, size=rowcol)


def generate_unit_matrix(rowcol: int):
    return np.identity(rowcol)


def generate_diagonal_matrix(rowcol: tuple[int, int]):
    matrix = np.zeros(rowcol)
    np.fill_diagonal(matrix, np.diag(generate_matrix(rowcol)))
    return matrix


def generate_triangular_uper_matrix(rowcol: int | tuple[int, int]):
    return np.triu(generate_matrix(rowcol))


def generate_triangular_lower_matrix(rowcol: int | tuple[int, int]):
    return np.triu(generate_matrix(rowcol))


def generate_binary_matrix(rowcol: tuple[int, int]):
    return None


print(generate_triangular_uper_matrix((5)))
