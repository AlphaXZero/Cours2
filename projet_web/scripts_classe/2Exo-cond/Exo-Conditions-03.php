<?php
$etatEbriete = readline("Quel était l'état d'ébriété du ministre (0 = sobre, 1 = joyeux, 2 = ivre) : ");
if ($etatEbriete == 0) {
    echo ("Le ministre était sobre et responsable !");
} elseif ($etatEbriete == 1) {
    echo ("Le ministre est joyeux !");
} elseif ($etatEbriete == 2) {
    echo ("Le ministre est ivre !");
} else {
    echo ("Erreur, état d'ebriété inconnu !");
}
