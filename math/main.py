import random

matrix = list[list[int | float]]


def print_matrix(matrix: matrix) -> None:
    """print a matrix in a human readable representation

    Args:
        matrix (list[list[int  |  float]]): the matrix we want to print
    """
    for row in matrix:
        print(" | ".join(list(map(str, row))))


def create_matrix(
    row: int, col: int, val_min: float = 0, val_max: float = 9, real_num: bool = False
) -> matrix:
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


def is_square_matrix(row: int, col: int) -> bool:
    return row == col


def create_unit_matrix(row: int, col: int) -> None | matrix:
    if not is_square_matrix(row, col):
        return None
    return [[1 if i == j else 0 for i in range(col)] for j in range(row)]


def create_diagonal_matrix(row: int, col: int) -> None | matrix:
    if not is_square_matrix(row, col):
        return None
    return [
        [random.randint(1, 9) if i == j else 0 for i in range(col)] for j in range(row)
    ]


def create_upper_triangular_matrix(row: int, col: int) -> None | matrix:
    if not is_square_matrix(row, col):
        return None
    return [
        [random.randint(1, 9) if i >= j else 0 for i in range(col)] for j in range(row)
    ]


def create_lower_triangular_matrix(row: int, col: int) -> None | matrix:
    if not is_square_matrix(row, col):
        return None
    return [
        [random.randint(1, 9) if i <= j else 0 for i in range(col)] for j in range(row)
    ]


def create_sparse_matrix(row: int, col: int) -> matrix:
    return create_matrix(row, col, 0, 1)


def create_zero_matrix(row: int, col: int) -> matrix:
    return create_matrix(row, col, 0, 0)


def show_matrix():
    """print a random matrix in the size and range wanted by the user"""
    print_matrix(
        create_matrix(
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
            create_unit_matrix,
            create_diagonal_matrix,
            create_upper_triangular_matrix,
            create_lower_triangular_matrix,
            create_sparse_matrix,
            create_zero_matrix,
        ]
    ):
        print(f"matrice {caption[i]} :")
        if func(row, col):
            print_matrix(func(row, col))
            print()
        else:
            print("impossible car la matrice n'est pas carré \n")


if __name__ == "__main__":
    # Exo1
    # user_create_matrix()

    # Exo2
    show_specials_matrix()
    pass
