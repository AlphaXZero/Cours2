<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function respecteLongueurMinEtMax($entreeutilisateur, $longueurMin, $longueurMax)
{
    $len = mb_strlen($entreeutilisateur);
    return ($len < $longueurMax && $len > $longueurMin);
}


// Appeler la fonction "respecteLongueurMinEtMax()" pour vérifier si le nombre de caractères de la chaîne "saperlipopette" est comprise entre 2 et 30 caractères.
$estLongueurValide = respecteLongueurMinEtMax("saperlipopette", 2, 30);
var_dump($estLongueurValide); // Affiche : bool(true)

// Appeler la fonction "respecteLongueurMinEtMax()" pour vérifier si le nombre de caractères de la chaîne "saperlipopette" est comprise entre 2 et 8 caractères.
$estLongueurValide = respecteLongueurMinEtMax("saperlipopette", 2, 8);
var_dump($estLongueurValide); // Affiche : bool(false)