import numpy as np


def generate_matrix(
    rowcol: tuple[int, int], min_val: int = 1, max_val: int = 20
) -> np.ndarray:
    return np.random.randint(min_val, max_val + 1, size=rowcol)


def generate_float_matrix(
    rowcol: tuple[int, int], min_val: int | float = 1, max_val: int | float = 20
) -> np.ndarray:
    return np.random.uniform(1, 20, size=rowcol)


def fill_matrix(matrix: np.ndarray) -> np.ndarray:
    values = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            values.append(int(input(f"m{row + 1}{col + 1} :")))
    return np.array(values).reshape(matrix.shape)


def generate_unit_matrix(rowcol: int) -> np.ndarray:
    return np.identity(rowcol)


def generate_diagonal_matrix(rowcol: tuple[int, int]) -> np.ndarray:
    matrix = np.zeros(rowcol)
    np.fill_diagonal(matrix, np.diag(generate_matrix(rowcol)))
    return matrix


def generate_triangular_uper_matrix(rowcol: int | tuple[int, int]) -> np.ndarray:
    return np.triu(generate_matrix(rowcol))


def generate_triangular_lower_matrix(rowcol: int | tuple[int, int]) -> np.ndarray:
    return np.tril(generate_matrix(rowcol))


def generate_binary_matrix(rowcol: tuple[int, int]) -> np.ndarray:
    return np.random.randint(0, 2, size=rowcol)


def generate_zero_matrix(rowcol: tuple[int, int]) -> np.ndarray:
    return np.zeros(rowcol)


def is_additionnable(matrix1: np.ndarray, matrix2: np.ndarray) -> bool:
    return matrix1.shape == matrix2.shape


def do_addition(matrix1: np.ndarray, matrix2: np.ndarray) -> None | np.ndarray:
    return np.add(matrix1, matrix2) if is_additionnable(matrix1, matrix2) else None


def is_multiplicable(matrix1: np.ndarray, matrix2: np.ndarray) -> bool:
    return len(matrix1[0]) == len(matrix2)


if __name__ == "__main__":
    oui = generate_matrix((3, 4))
    print(oui)
