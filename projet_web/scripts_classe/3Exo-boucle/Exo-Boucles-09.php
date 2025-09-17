<?php
$matriceHauteurLargeur = 4;
$resultat = "";

for ($i = 1; $i < $matriceHauteurLargeur * $matriceHauteurLargeur; $i += $matriceHauteurLargeur) {
    for ($j = 0; $j < $matriceHauteurLargeur; $j++) {
        $resultat .= "-" . ($i + $j) . "- ";
    }
    $resultat .= "\n";
}
echo $resultat;
