<?php
$estPresent = true;
$aFaitPipi = true;
$estEmeche = false;

if ($estPresent) {
    if ($aFaitPipi) {
        if ($estEmeche) {
            echo ("Le ministre ne se souvient pas de tout à cause de son état d'ébriété.");
        } else {
            echo ("Le ministre était en train de jouer un air de guitare devant ses invités.");
        }
    } else {
        echo ("Le ministre était là, mais il ne savait rien des agissements de ses invités.");
    }
} else {
    echo ("Le ministre n'était pas là pendant l'incident.");
}
