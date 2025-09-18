<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function estRempli($nomDuChampnom, $entreesUtilisateur)
{
    if (array_key_exists($nomDuChampnom, $entreesUtilisateur)) {
        $actu_key = trim($entreesUtilisateur[$nomDuChampnom]);
        if (!empty($actu_key)) {
            return True;
        }
    }
    return False;
}
// isset($entree["nom"])

// Simulation d'entrées utilisateur provenant d'un formulaire.
$entreesUtilisateur = [
    'nom' => 'Claudy',
    'email' => 'claudy.focan@gmail.com'
];

// Appeler la fonction "estRempli()" pour vérifier que le champ requis nommé "nom" a bien été rempli.
$estNomRempli = estRempli("nom", $entreesUtilisateur);
var_dump($estNomRempli); // Affiche : bool(true)

// Appeler la fonction "estRempli()" pour vérifier que le champ requis nommé "prenom" a bien été rempli.
$estPrenomRempli = estRempli("prenom", $entreesUtilisateur);
var_dump($estPrenomRempli); // Affiche : bool(false)