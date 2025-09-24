<?php

declare(strict_types=1);

function afficherMoyenne($nombres)
{
    if (count($nombres) == 0) {
        return 0;
    }
    echo implode(" ", $nombres) . PHP_EOL;
    return array_sum($nombres) / count($nombres);
}
$listeDeNombres = [8, 7, 6.5, 4.5, 7, 8];

echo afficherMoyenne($listeDeNombres);
