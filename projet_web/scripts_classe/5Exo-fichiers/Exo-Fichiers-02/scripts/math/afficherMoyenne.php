<?php
require_once "calculerMoyenne.php";
function afficherMoyenne($nombres)
{
    $avg = calculerMoyenne($nombres)[0];
    $valid_nbr = calculerMoyenne($nombres)[1];
    $invalid_nbr = array_diff($nombres, $valid_nbr);
    print_r($valid_nbr);
    print_r($invalid_nbr);
    echo "moyenne : $avg";
}
