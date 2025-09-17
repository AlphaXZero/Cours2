<?php
$matrice = [
    ['-1-', '-2-', '-3-'],
    ['-4-', '-5-', '-6-'],
    ['-7-', '-8-', '-9-']
];
$resultat = "";

foreach ($matrice as $row) {
    foreach ($row as $value) {
        $resultat .= $value . " ";
    }
    $resultat .= PHP_EOL;
}
echo $resultat;
