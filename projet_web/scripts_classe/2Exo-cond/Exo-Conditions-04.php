<?php
$etatEbriete = readline("Quel était l'état d'ébriété du ministre (0 = sobre, 1 = joyeux, 2 = ivre) : ");
switch ($etatEbriete) {
    case "0":
        echo ("Le ministre était sobre et responsable !\n");
        break;
    case "1":
        echo ("Le ministre est joyeux !\n");
        break;
    case "2":
        echo ("Le ministre est ivre !\n");
        break;
    default:
        echo ("Erreur, état d'ebriété inconnu !\n");
}
