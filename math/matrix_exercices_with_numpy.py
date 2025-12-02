from logical_matrix_numpy import (
    generate_matrix,
    generate_float_matrix,
    generate_binary_matrix,
    generate_diagonal_matrix,
    generate_triangular_lower_matrix,
    generate_triangular_uper_matrix,
    generate_unit_matrix,
    generate_zero_matrix,
    fill_matrix,
    do_addition,
    is_multiplicable,
    get_col_sum,
    get_row_sum,
    do_exponent_matrix,
)
import random


def do_exercise_1():
    print("Exercice I")
    print("-------------")
    rowcol = (
        int(input("Entrez le nombre de lignes souhaité: ")),
        int(input("Entre le nombre de colonnes souhaité: ")),
    )
    print(f"\nmatrice avec des entiers :\n {generate_matrix(rowcol)}")
    print(f"\nmatrice avec des réels :\n {generate_float_matrix(rowcol)}")
    print("-------------")


def do_exercise_2():
    print("Exercice II")
    print("-------------")
    rowcol = (
        int(input("\nEntrez le nombre de lignes souhaité: ")),
        int(input("Entrez le nombre de colonnes souhaité: ")),
    )
    caption = [
        "identité",
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
            generate_triangular_uper_matrix,
            generate_triangular_lower_matrix,
            generate_binary_matrix,
            generate_zero_matrix,
        ]
    ):
        print(f"matrice {caption[i]}: ")
        if func == generate_unit_matrix:
            print(
                "impossible car matrice non carré"
                if rowcol[0] != rowcol[1]
                else func(rowcol[0])
            )
        else:
            print(func(rowcol))
        print("-------------")


def do_exercise_3():
    print("Exercice III")
    print("-------------")
    rowcol = (
        int(input("Entrez le nombre de lignes souhaité: ")),
        int(input("Entrez le nombre de colonnes souhaité: ")),
    )
    print("\npremière matrice:")
    matrix1 = fill_matrix(generate_zero_matrix(rowcol))
    print(matrix1)
    print("deuxième matrice:")
    matrix2 = fill_matrix(generate_zero_matrix(rowcol))
    print(matrix2)
    print("somme des matrices:")
    print(do_addition(matrix1, matrix2))


def do_exercise_4():
    print("Ecxercice IV")
    print("-------------")
    matrix = generate_matrix((random.randint(1, 7), random.randint(1, 7)))
    opposite_matrix = -matrix
    print(f"matrice de base: \n {matrix}")
    print(f"matrice opposée: \n {opposite_matrix}")
    print(f"somme des 2 matrices:\n {do_addition(matrix, opposite_matrix)}")


def do_exercise_5():
    print("Exercice V")
    print("-------------")
    matrix = generate_matrix((random.randint(1, 7), random.randint(1, 7)))
    print(f"matrice aléatoire:\n {matrix}")
    scalar_input = int(input("Entrez un entier qui multipliera la matrice: "))
    print(f"matrice résultat :\n {matrix * scalar_input}")


def do_exercise_6():
    print("Exercice VI")
    print("-------------")
    print("\npremière matrice:")
    rowcol = (
        int(input("Entrez le nombre de lignes souhaité: ")),
        int(input("Entrez le nombre de colonnes souhaité: ")),
    )
    matrix1 = fill_matrix(generate_zero_matrix(rowcol))
    print(matrix1)
    print("deuxième matrice:")
    rowcol = (
        int(input("Entrez le nombre de lignes souhaité: ")),
        int(input("Entrez le nombre de colonnes souhaité: ")),
    )
    matrix2 = fill_matrix(generate_zero_matrix(rowcol))
    print(matrix2)
    print("\nmutliplicatoin des 2 matrices: ")
    if is_multiplicable(matrix1, matrix2):
        print(matrix1 @ matrix2)
    else:
        print("tailes non compatibles")


def do_exercise_7():
    print("Exercice VII")
    print("-------------")
    matrix = generate_matrix((random.randint(1, 7), random.randint(1, 7)))
    print(f"matrice aléatoire:\n {matrix}")
    print(f"somme des colonnes:\n {get_col_sum(matrix)}")


def do_exercise_8():
    print("Exercice VIII")
    print("-------------")
    matrix = generate_matrix((random.randint(1, 7), random.randint(1, 7)))
    print(f"matrice aléatoire:\n {matrix}")
    print(f"somme des lignes:\n {get_row_sum(matrix).reshape((matrix.shape[0], 1))}")


def do_exercise_9():
    print("Exercice IX")
    print("-------------")
    random_row = random.randint(1, 7)
    matrix = generate_matrix(((random_row, random_row)))
    print(f"matrice carré aléatoire:\n{matrix}")
    power = int(input("qu'elle puissance souhaitez vous ?"))
    print(do_exponent_matrix(matrix, power))


def do_exercise_10():
    print("Exercice IX")
    print("-------------")
    rowcol1 = (
        int(input("Entrez le nombre de lignes souhaité pour la matrice A: ")),
        int(input("Entrez le nombre de colonnes souhaité pour la matrice A: ")),
    )
    rowcol2 = (
        int(input("Entrez le nombre de lignes souhaité pour la matrice B: ")),
        int(input("Entrez le nombre de colonnes souhaité pour la matrice B: ")),
    )
    if rowcol1 != rowcol2:
        print("impossible car tailles différentes")
    else:
        print("\npremière matrice:")
        matrix1 = fill_matrix(generate_zero_matrix(rowcol1), "A")
        print(matrix1)
        print("deuxième matrice:")
        matrix2 = fill_matrix(generate_zero_matrix(rowcol2), "B")
        print(matrix2)
        print("prosuit d'Hadamard:")
        print(matrix1 * matrix2)


if __name__ == "__main__":
    # do_exercise_1()
    # do_exercise_2()
    # do_exercise_3()
    # do_exercise_4()
    # do_exercise_6()
    # do_exercise_7()
    # do_exercise_8()
    # do_exercise_9()
    do_exercise_10()
    pass
