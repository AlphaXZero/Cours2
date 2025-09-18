<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function calculerMontantTvaPrixTTC($prixTtc, $tva)
{
    return ($prixTtc * $tva) / (100 + $tva);
}

function retirerTva($prixTtc, $tva)
{
    return round($prixTtc - calculerMontantTvaPrixTTC($prixTtc, $tva), 3);
}

// Afficher le prix HT d'un article de 100 euros TTC, la TVA est de 21%.
echo retirerTva(100, 21) . PHP_EOL; // Affiche : 82.645

// Afficher le prix HT d'un article de 100 euros TTC, la TVA est de 12%.
echo retirerTva(100, 12) . PHP_EOL; // Affiche : 89.286