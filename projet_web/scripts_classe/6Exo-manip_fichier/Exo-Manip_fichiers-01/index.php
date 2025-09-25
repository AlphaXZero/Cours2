<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);
require_once "./fonctions/afficherElementsFichier.php";
require_once "./fonctions/ecrireElementsDansFichier.php";
// Le tableau avec les phrases devant être ajoutée au fichier désiré.
$listeDePhrases = [
    "Claudy aime les poneys.",
    "Jean-Claude est nerveux.",
    "Laurence n'aime pas les kékés.",
    "Steph est l'ami de Jean-Claude."
];

// Le nom du fichier que l'on désire créer.
$nomFichier = "./textes/Exo_manipulation_de_fichiers_1.txt";

// Appeler la fonction "ecrireElementsDansFichier()" pour créer le fichier et y écrire les phrases du tableau "$listeDePhrases".
ecrireElementsDansFichier($nomFichier, $listeDePhrases);

// Afficher le contenu d'un fichier ligne par ligne avec la fonction "afficherElementsFichier()".
afficherElementsFichier($nomFichier);
/*
    Affiche :
    Claudy aime les poneys.
    Jean-Claude est nerveux.
    Laurence n'aime pas les kékés.
    Steph est l'ami de Jean-Claude.
*/