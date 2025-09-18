<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function respecteLongueurMinimale($entreeutilisateur, $longueurMin)
{
    return mb_strlen($entreeutilisateur) > $longueurMin;
}
// Appeler la fonction "respecteLongueurMinimale()" pour vérifier si la chaîne "saperlipopette" possède au moins 2 caractères.
$estLongueurValide = respecteLongueurMinimale("saperlipopette", 2);
var_dump($estLongueurValide); // Affiche : bool(true)

// Appeler la fonction "respecteLongueurMinimale()" pour vérifier si la chaîne "saperlipopette" possède au moins 30 caractères.
$estLongueurValide = respecteLongueurMinimale("saperlipopette", 30);
var_dump($estLongueurValide); // Affiche : bool(false)