from logical_matrix_without_numpy import *

if __name__ == "__main__":
    # Exo1
    # show_matrix()

    # Exo2
    # show_specials_matrix()

    # Exo 3
    # row1, col1 = (
    #     int(input("Entrez le nombre de lignes souhaités pour la matrice1: ")),
    #     int(input("Entrez le nombre de colonnes souhaités pour la matrice1: ")),
    # )
    # matrix1 = create_matrix(row1, col1)
    # matrix1 = enter_values(matrix1)
    # row2, col2 = (
    #     int(input("Entrez le nombre de lignes souhaités pour la matrice1: ")),
    #     int(input("Entrez le nombre de colonnes souhaités pour la matrice1: ")),
    # )
    # matrix2 = create_matrix(row2, col2)
    # matrix2 = enter_values(matrix2)
    # print("première matrice: ")
    # print_matrix(matrix1)
    # print("------------")
    # print("deuxième matrice: ")
    # print_matrix(matrix2)
    # if not is_same_size(matrix1, matrix2):
    #     print("taille différentes, addition/soustraction impossible")
    # else:
    #     print("------------")
    #     print("somme des matrices: ")
    #     print_matrix(add_matrix(matrix1, matrix2))
    #     print("------------")
    #     print("différence des matrices: ")
    #     print_matrix(subtract_matrix(matrix1, matrix2))

    # Exo 4
    # matrix = create_matrix(3, 3)
    # print("matrice aléatoire: ")
    # print_matrix(matrix)
    # print("------------")
    # print("Matrice opposée: ")
    # opposite = calculate_opposite_matrix(matrix)
    # print("------------")
    # print("somme de la matrice + opposée")
    # print_matrix(add_matrix(matrix, opposite))

    # Exo 5
    # matrix = create_random_matrix()
    # print("matrice: ")
    # print_matrix(matrix)
    # print("------------")
    # scalar = int(input("Entrez un nombre qui multiplira la matrice: "))
    # print("------------")
    # print_matrix(calculate_scalar_product(matrix, scalar))

    # Exo 6
    # matrix1 = create_random_matrix()
    # matrix2 = create_random_matrix()
    # matrix1 = [[-2, 1, 1], [-1, 3, 2]]
    # matrix2 = [[3, 0, -2, 1], [2, -4, 1, 3], [-1, 2, 0, -2]]
    # print("première matrice : ")
    # print_matrix(matrix1)
    # print("------------")
    # print("deuxième matrice : ")
    # print_matrix(matrix2)
    # print("------------")
    # print("résultat : ")
    # if not is_multicplicable(matrix1, matrix2):
    #     print("Impossible")
    # else:
    #     print_matrix(calculate_multiplication(matrix1, matrix2))

    # Exo 7
    # matrix1 = [[-2, 1, 1], [-1, 3, 2]]
    # print("matrice : ")
    # print_matrix(matrix1)
    # print("------------")
    # print(calculate_row_sum(matrix1))

    # Exo 8
    # matrix1 = [[-2, 1, 1], [-1, 3, 2]]
    # print("matrice : ")
    # print_matrix(matrix1)
    # print("------------")
    # print(calculate_col_sum(matrix1))

    # Exo 9
    matrix1 = generate_matrix(4, 4)
    print_matrix(matrix1)
    print("-------")
    print_matrix(do_exponent_matrix(matrix1, 2))

    # Exo 10
    # matrix1 = create_matrix(4, 4)
    # matrix2 = create_matrix(4, 4)
    # print("première matrice : ")
    # print_matrix(matrix1)
    # print("------------")
    # print("deuxième matrice : ")
    # print_matrix(matrix2)
    # print("------------")
    # print("résultat : ")
    # if not is_same_size(matrix1, matrix2):
    #     print("Impossible")
    # else:
    #     print_matrix(calculate_hadamard_multiplication(matrix1, matrix2))

    # Exo 11
    # matrix1 = create_random_matrix()
    # print_matrix(matrix1)
    # print("------------")
    # matrix1 = transpose_matrix(matrix1)
    # print_matrix(matrix1)
