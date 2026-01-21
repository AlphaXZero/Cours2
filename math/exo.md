exo 1
ordre 6
trois paires de sommets adjacents {1,2},{2,3},{3,4}
trois parires de sommets non-asjacents {5,6},{4,1},{5,4}
degré sommet 1 = 4
degré sommet 3 = 3
degré sommet 5 = 1
degré sommet 6 = 2
taille (nbr aretes) = 7
somme des dégrés de tous les sommets = 14

exo 2
0 1 0 0 
1 1 1 1
0 1 0 1
0 1 1 0


exo3
0 0 1 1
1 0 0 0
0 1 0 1
0 1 0 0

exo4
0 1 1 0
0 0 1 1
0 0 0 1
0 0 0 0

exo5 
toutes mais 1 et 3 ne peuvent pas être non orienté

exo6
3


exo7

0 0 0 0 1 0 1 0
0 0 0 0 1 1 0 0
0 0 0 1 0 1 1 1
0 0 1 0 0 1 1 1
1 1 0 0 0 0 0 0
0 1 1 1 0 0 0 1
1 0 1 1 0 0 0 1
0 0 1 1 0 1 1 0

exo8

11 car la matrice 3 donne le nombre de chemins de 3

exo 9
G1
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 1 0 0 0

G2
0 1 1 0 0
1 0 0 0 0
0 1 0 0 0
0 0 1 1 1
0 0 0 1 0

G1 U G2
0 1 1 0 0
1 0 1 0 0
0 1 0 1 0
0 0 1 1 1
1 1 0 1 0

g1 interserc g2
0 1 0 0 0
0 0 0 0 0 
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0

g1 produit g2
1 0 0 0 0
0 1 0 0 0
0 0 1 1 1
0 0 0 1 0
1 1 1 0 0

g1 inverse
0 0 0 0 1
1 0 0 0 1
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0 

g1 complément
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
0 0 1 1 1

dijkstra en partant de E
  D B E C F A
E 1 1 0 3 5 i
D 1 1 0 3 5 i
B 1 1 0 3 5 i
C 1 1 0 3 4 6
F 1 1 0 3 4 5
A 1 1 0 3 4 5