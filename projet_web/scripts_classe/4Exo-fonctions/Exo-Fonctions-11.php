<?php
// Appliquer la déclaration stricte des types.
declare(strict_types=1);

function estValideEmail($email)
{
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return true;
    }
    return false;
}

function respecteLongueurMinimale($entreeutilisateur, $longueurMin)
{
    return mb_strlen($entreeutilisateur) >= $longueurMin;
}

function respecteLongueurMaximale($entreeutilisateur, $longueurMax)
{
    return mb_strlen($entreeutilisateur) <= $longueurMax;
}

function respecteLongueurMinEtMax($entreeutilisateur, $longueurMin, $longueurMax)
{
    $len = mb_strlen($entreeutilisateur);
    return ($len <= $longueurMax && $len >= $longueurMin);
}

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

function verifierValiditeChamps($regleDesChamps, $entreesUtilisateur)
{
    $messagesErreur = [];
    foreach ($regleDesChamps as $cle => $regle) {
        if (
            isset($regle["requis"]) && $regle["requis"] == true
            && !isset($entreesUtilisateur[$cle])
        ) {

            $messagesErreur[$cle] = "Le champ $cle est requis!";
        } else {
            if (
                isset($regle["type"])
                && $regle["type"] == "email"
                && !estValideEmail($entreesUtilisateur[$cle])
            ) {
                $messagesErreur[$cle] = "Email invalide!";
            }
            if (
                isset($regle["longueurMin"])
                && isset($regle["longueurMax"])
                && (!respecteLongueurMinEtMax($entreesUtilisateur[$cle], $regle["longueurMin"], $regle["longueurMax"]))
            ) {
                $messagesErreur[$cle] = "Ce champ doit comprendre entre 
                {$regle["longueurMin"]} et {$regle["longueurMax"]} caractères !";
            } else if (
                isset($regle["longueurMin"])
                && !respecteLongueurMinimale($entreesUtilisateur[$cle], $regle["longueurMin"])
            ) {
                $messagesErreur[$cle] = "Ce champ doit comprendre au moins 
                {$regle["longueurMin"]} caractères!";
            } else if (
                isset($regle["longueurMax"])
                && !respecteLongueurMaximale($entreesUtilisateur[$cle], $regle["longueurMax"])
            ) {
                $messagesErreur[$cle] = "Ce champ doit comprendre au maximum 
                {$regle["longueurMax"]} caractères!";
            }
        }
    }
    return $messagesErreur;
}

// Les règles des champs du formulaires
$regleDesChamps = [
    'nom' => [
        'requis' => true,
        'longueurMin' => 2,
        'longueurMax' => 255
    ],
    'email' => [
        'requis' => true,
        'type' => 'email'
    ]
];

// Simulation d'entrées utilisateur valides provenant d'un formulaire.
$entreesUtilisateurValides = [
    'nom' => 'Cd',
    'email' => 'claudy.focan@gmail.com'
];

// Simulation d'entrées utilisateur invalides provenant d'un formulaire.
$entreesUtilisateurInvalides = [
    'email' => 'claudy.focan'
];


// Appeler la fonction "verifierValiditeChamps()" pour vérifier si les entrées utilisateurs respectent les règles de champ du formulaire.
$erreurs = verifierValiditeChamps($regleDesChamps, $entreesUtilisateurValides);
print_r($erreurs);
/*
    Affiche :
        Array
        (
        )
*/

// Appeler la fonction "verifierValiditeChamps()" pour vérifier si les entrées utilisateurs respectent les règles de champ du formulaire.
$erreurs = verifierValiditeChamps($regleDesChamps, $entreesUtilisateurInvalides);
print_r($erreurs);
/*
    Affiche :
        Array
        (
            [nom] => Ce champs est requis!
            [email] => Email invalide!
        )
*/