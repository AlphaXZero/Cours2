from matrix_numpy import (
    generate_matrix,
    generate_float_matrix,
    generate_binary_matrix,
    generate_diagonal_matrix,
    generate_triangular_lower_matrix,
    generate_triangular_uper_matrix,
    generate_unit_matrix,
    generate_zero_matrix,
)


def do_exercise_1():
    print("Exercice I")
    print("-------------")
    row = int(input("Entrez le nombre de lignes souhaité: "))
    col = int(input("Entre le nombre de colonnes souhaité: "))
    print(f"\nmatrice avec des entiers :\n {generate_matrix((row, col))}")
    print(f"\nmatrice avec des réels :\n {generate_float_matrix((row, col))}")
    print("-------------")


def do_exercise_2():
    print("Exercice II")
    print("-------------")
    row = int(input("\nEntrez le nombre de lignes souhaité: "))
    col = int(input("Entrez le nombre de colonnes souhaité: "))
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
            print("impossible car matrice non carré" if row != col else func(row))
        else:
            print(func((row, col)))
        print("-------------")


if __name__ == "__main__":
    do_exercise_2()
