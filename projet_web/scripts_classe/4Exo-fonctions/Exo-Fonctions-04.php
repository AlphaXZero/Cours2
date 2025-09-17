<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function calculerMontantTvaPrixHT($prixHt, $tva): float|int
{
    return $prixHt * ($tva / 100);
}

function ajouterTva($prixHt, $tva)
{
    return round($prixHt + calculerMontantTvaPrixHT($prixHt, $tva), 3);
}

// Afficher le prix TTC d'un article de 100 euros HT, la TVA est de 21%.
echo ajouterTva(100, 21) . PHP_EOL; // Affiche : 121

// Afficher le prix TTC d'un article de 100 euros HT, la TVA est de 12%.
echo ajouterTva(100, 12) . PHP_EOL; // Affiche : 112