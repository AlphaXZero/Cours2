<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function respecteLongueurMaximale($entreeutilisateur, $longueurMax)
{
    return mb_strlen($entreeutilisateur) < $longueurMax;
}

// Appeler la fonction "respecteLongueurMaximale()" pour vérifier si la chaîne "saperlipopette" ne dépasse pas la limites de 30 caractères.
$estLongueurValide = respecteLongueurMaximale("saperlipopette", 30);
var_dump($estLongueurValide); // Affiche : bool(true)

// Appeler la fonction "respecteLongueurMaximale()" pour vérifier si la chaîne "saperlipopette" ne dépasse pas les limites de 2 caractères.
$estLongueurValide = respecteLongueurMaximale("saperlipopette", 2);
var_dump($estLongueurValide); // Affiche : bool(false)