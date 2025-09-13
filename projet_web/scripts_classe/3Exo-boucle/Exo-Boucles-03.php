<?php
$nombreMystere = rand(1, 20);
$entree = 0;
$compteur = 1;

while (true) {
    $entree = readline("Entrez un nombre entre 1 et 20 : ");
    if (is_numeric($entree) && $entree > 0 && $entree <= 20) {
        if ($entree == $nombreMystere) {
            echo ("Vous avez trouvé en {$compteur} tentatives\n");
            break;
        } elseif ($entree > $nombreMystere) {
            echo ("Le nombre mystère est plus petit!\n");
        } elseif ($entree < $nombreMystere) {
            echo ("Le nombre mystère est plus grand!\n");
        }
        $compteur++;
    } else {
        echo ("Entrée incorecte\n");
    }
}
