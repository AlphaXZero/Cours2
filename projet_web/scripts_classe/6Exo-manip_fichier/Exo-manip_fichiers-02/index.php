<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

// Déclare une constante DS pour représenter le séparateur de répertoire du système d'exploitation actuel.
define("DS", DIRECTORY_SEPARATOR);

require_once "./fonctions/enregistrerTableauEnJson.php";
require_once "./fonctions/importerJsonEnTableau.php";

// Chemin vers le dictionnaire au format JSON.
$cheminDictionnaire = __DIR__ . DS . 'bdd' . DS . 'dictionnaire.json';

// Convertir le contenu du fichier JSON en tableau associatif.
$dictionnaire = importerJsonEnTableau($cheminDictionnaire);
print_r($dictionnaire);
// Ajouter une valeur dans chacune des catégories :
$dictionnaire['nourriture'][] = 'poire';
$dictionnaire['animaux'][] = 'grenouille';
$dictionnaire['professions'][] = 'couvreur';

// Convertir et enregistrer le tableau au format JSON dans le fichier de destination.
enregistrerTableauEnJson($cheminDictionnaire, $dictionnaire);
