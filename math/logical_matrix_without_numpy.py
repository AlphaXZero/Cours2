import random
import time

MatrixType = list[list[int | float]]


def print_matrix(matrix: MatrixType) -> None:
    """print a matrix in a human readable representation

    Args:
        matrix (list[list[int  |  float]]): the matrix we want to print
    """
    for row in matrix:
        print(" | ".join(list(map(str, row))))


def generate_matrix(
    row: int, col: int, val_min: float = 0, val_max: float = 9, real_num: bool = False
) -> MatrixType:
    """create a matrix with random values within

    Args:
        rows (int): amount of rows
        col (int): amount of columns
        val_min (float): minimal value for the values in the matrix
        val_max (float): maximal value for the values in the matrix
        real_num (bool, optional): if True set of reals, set of intergers otherwise. Defaults to False.
    """
    return [
        [
            round(random.uniform(val_min, val_max), 2)
            if real_num
            else random.randint(int(val_min), int(val_max))
            for i in range(col)
        ]
        for j in range(row)
    ]


def create_random_matrix() -> MatrixType:
    return generate_matrix(random.randint(2, 10), random.randint(2, 10))


def fill_matrix(matrix: MatrixType) -> MatrixType:
    edited_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            edited_matrix[i][j] = int(input(f"Entre la valeur m{i + 1}{j + 1}: "))
    return edited_matrix


def is_square_matrix(row: int, col: int) -> bool:
    return row == col


def generate_unit_matrix(row: int, col: int) -> None | MatrixType:
    if not is_square_matrix(row, col):
        return None
    return [[1 if i == j else 0 for i in range(col)] for j in range(row)]


def generate_diagonal_matrix(row: int, col: int) -> None | MatrixType:
    if not is_square_matrix(row, col):
        return None
    return [
        [random.randint(1, 9) if i == j else 0 for i in range(col)] for j in range(row)
    ]


def generate_upper_triangular_matrix(row: int, col: int) -> None | MatrixType:
    if not is_square_matrix(row, col):
        return None
    return [
        [random.randint(1, 9) if i >= j else 0 for i in range(col)] for j in range(row)
    ]


def generate_lower_triangular_matrix(row: int, col: int) -> None | MatrixType:
    if not is_square_matrix(row, col):
        return None
    return [
        [random.randint(1, 9) if i <= j else 0 for i in range(col)] for j in range(row)
    ]


def generate_sparse_matrix(row: int, col: int) -> MatrixType:
    return generate_matrix(row, col, 0, 1)
    # return [
    #     [
    #         random.choices([0, random.randint(1, 9)], weights=[0.8, 0.2], k=1)[0]
    #         for i in range(col)
    #     ]
    #     for j in range(row)
    # ]


def generate_zero_matrix(row: int, col: int) -> MatrixType:
    return generate_matrix(row, col, 0, 0)


def show_matrix():
    """print a random matrix in the size and range wanted by the user"""
    print_matrix(
        generate_matrix(
            int(input("Entrez le nombre de lignes souhaité: ")),
            int(input("Entrez le nombre de colonnes souhaité: ")),
            float(input("Entrez le nombre de minimal souhaité: ")),
            float(input("Entrez le nombre de maximal souhaité: ")),
            True
            if input(
                "Entrez 1 pour l'ensemble des réels ou 0 pour l'ensemble des entiers: "
            )
            == "1"
            else False,
        )
    )


def show_specials_matrix():
    row = int(input("Entrez le nombre de lignes souhaité: "))
    col = int(input("Entrez le nombre de colonnes souhaité: "))
    caption = [
        "unité",
        "diagonale",
        "triangulaire supérieur",
        "triangulaire inférieur",
        "creuse",
        "nulle",
    ]
    for i, func in enumerate(
        [
            generate_unit_matrix,
            generate_diagonal_matrix,
            generate_upper_triangular_matrix,
            generate_lower_triangular_matrix,
            generate_sparse_matrix,
            generate_zero_matrix,
        ]
    ):
        print(f"matrice {caption[i]} :")
        if func(row, col):
            print_matrix(func(row, col))
            print()
        else:
            print("impossible car la matrice n'est pas carré \n")


def is_same_size(matrix1: MatrixType, matrix2: MatrixType) -> bool:
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])


def add_matrix(matrix1: MatrixType, matrix2: MatrixType) -> None | MatrixType:
    if not is_same_size(matrix1, matrix2):
        return None
    matrix_out = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix_out[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix_out


def calculate_opposite_matrix(matrix: MatrixType) -> MatrixType:
    return [[-i for i in j] for j in matrix]


def calculate_scalar_product(matrix: MatrixType, scalar: int) -> MatrixType:
    return [[i * scalar for i in j] for j in matrix]


def subtract_matrix(matrix1: MatrixType, matrix2: MatrixType) -> None | MatrixType:
    if not is_same_size(matrix1, matrix2):
        return None
    return add_matrix(matrix1, calculate_opposite_matrix(matrix2))


def is_multicplicable(matrix1: MatrixType, matrix2: MatrixType) -> bool:
    return len(matrix1[0]) == len(matrix2)


def calculate_multiplication(
    matrix1: MatrixType, matrix2: MatrixType
) -> None | MatrixType:
    # if not is_multicplicable(matrix1, matrix2):
    #     return None
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[0])):
            result_matrix[i][j] = sum(
                [x * y for x, y in zip(matrix1[i], [row[j] for row in matrix2])]
            )
    return result_matrix


def calculate_row_sum(matrix: MatrixType) -> list:
    row_sum = []
    for i in matrix:
        row_sum.append(sum(i))
    return row_sum


def calculate_col_sum(matrix: MatrixType) -> list:
    col_sum = []
    for i in range(len(matrix[0])):
        col_sum.append(sum([row[i] for row in matrix]))
    return col_sum


def calculate_hadamard_multiplication(
    matrix1: MatrixType, matrix2: MatrixType
) -> MatrixType:
    if not is_same_size(matrix1, matrix2):
        return None
    matrix_out = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix_out[i][j] = matrix1[i][j] * matrix2[i][j]
    return matrix_out


def transpose_matrix(matrix: MatrixType) -> MatrixType:
    result_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result_matrix[i][j] = matrix[j][i]
    return result_matrix


def do_exponent_matrix(matrix: MatrixType, exponent: int) -> MatrixType:
    result = [[i for i in row] for row in matrix]
    for i in range(exponent - 1):
        result = add_matrix(result, result)
    return result
