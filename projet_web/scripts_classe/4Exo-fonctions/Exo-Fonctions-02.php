<?php

declare(strict_types=1);

function calculerMoyenne($nombres)
{
    if (count($nombres) == 0) {
        return 0;
    }
    return array_sum($nombres) / count($nombres);
}
function convertirTableauEnChaineDeCaracteres($nombres)
{
    return implode(" ", $nombres);
}

$listeDeNombres = [8, 7, 6.5, 4.5, 7, 8];
$moyenne = calculerMoyenne($listeDeNombres);
$listeDeNombres = convertirTableauEnChaineDeCaracteres($listeDeNombres);
echo "La moyenne des nombres [ $listeDeNombres ] : $moyenne";
