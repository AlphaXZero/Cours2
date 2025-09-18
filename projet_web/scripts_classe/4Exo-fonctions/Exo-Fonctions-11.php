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
    return mb_strlen($entreeutilisateur) > $longueurMin;
}

function respecteLongueurMaximale($entreeutilisateur, $longueurMax)
{
    return mb_strlen($entreeutilisateur) < $longueurMax;
}

function respecteLongueurMinEtMax($entreeutilisateur, $longueurMin, $longueurMax)
{
    $len = mb_strlen($entreeutilisateur);
    return ($len < $longueurMax && $len > $longueurMin);
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
        if (isset($regle["requis"]) && empty($regleDesChamps[$cle])) {
            $messagesErreur[$cle] = "Le champ est $cle requis!";
        } else {
            if (in_array("type", $regle) && $regle["type"] == "email" && !estValideEmail($regle)) {
                $messagesErreur[$cle] = "Email invalide!";
            } else if ($cle == "longueurMin" && $cle == "longueurMax") {
            }
        }
    }
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
    'nom' => 'Claudy',
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