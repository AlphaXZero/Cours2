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

// Appeler la fonction "estValideEmail()" pour vérifier si l'adresse email "claudy.focan@gmail.com" est valide.
$estEmailRempli = estValideEmail("claudy.focan@gmail.com");
var_dump($estEmailRempli); // Affiche : bool(true)

// Appeler la fonction "estValideEmail()" pour vérifier si l'adresse email "claudy.focan" est valide.
$estEmailRempli = estValideEmail("claudy.focan");
var_dump($estEmailRempli); // Affiche : bool(false)