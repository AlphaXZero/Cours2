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
)


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


if __name__ == "__main__":
    # do_exercise_1()
    # do_exercise_2()
    # do_exercise_3()

    pass
