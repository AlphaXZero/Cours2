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


if __name__ == "__main__":
    # do_exercise_1()
    # do_exercise_2()
    # do_exercise_3()
    # do_exercise_4()
    # do_exercise_6()
    pass
