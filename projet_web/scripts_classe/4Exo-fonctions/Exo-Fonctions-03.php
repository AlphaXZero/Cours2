<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function calculerSomme($nombres)
{
    $sum = 0;
    $valid_nbr = [];
    foreach ($nombres as $nbr) {

        if (is_int($nbr) || is_float($nbr)) {
            $sum += $nbr;
            $valid_nbr[] = $nbr;
        }
    }
    return [$sum, $valid_nbr];
}
function calculerMoyenne($nombres)
{
    $valid_nbr = calculerSomme($nombres)[1];
    return [calculerSomme($nombres)[0] / count($valid_nbr), $valid_nbr];
}

function convertirTableauEnChaineDeCaracteres($nombres)
{
    return implode(", ", $nombres);
}

function afficherMoyenne($nombres)
{
    $avg = calculerMoyenne($nombres)[0];
    $valid_nbr = calculerMoyenne($nombres)[1];
    $invalid_nbr = array_diff($nombres, $valid_nbr);
    print_r($valid_nbr);
    print_r($invalid_nbr);
    echo "moyenne : $avg";
}

// Le tableau dont en veut calculer la moyenne.
$listeDeNombres = [8, 'trois', 7, 6.5, 'cinq', 4.5, 7, 8];
// Appeler la fonction "afficherMoyenne()" pour calculer et afficher les nombres présents dans le tableau "$listeDeNombres".
afficherMoyenne($listeDeNombres);
/*
    Affiche :
        La moyenne des nombres [ 8, 7, 6.5, 4.5, 7, 8 ] : 6.8333333333333
        Les valeurs ayant été rejetées ['trois', 'cinq']
*/