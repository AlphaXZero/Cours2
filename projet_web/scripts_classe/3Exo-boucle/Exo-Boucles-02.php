<?php
$valDebut = 15;
$valFin = 20;

if ($valDebut < $valFin) {
    while ($valDebut <= $valFin) {
        echo ("$valDebut \n");
        $valDebut++;
    }
} else if ($valDebut > $valFin) {
    while ($valDebut >= $valFin) {
        echo ("$valDebut \n");
        $valDebut--;
    }
}
