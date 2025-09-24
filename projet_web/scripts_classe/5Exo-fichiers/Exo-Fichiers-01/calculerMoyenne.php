<?php
require_once "calculerSomme.php";
function calculerMoyenne($nombres)
{
    $valid_nbr = calculerSomme($nombres)[1];
    return [calculerSomme($nombres)[0] / count($valid_nbr), $valid_nbr];
}
