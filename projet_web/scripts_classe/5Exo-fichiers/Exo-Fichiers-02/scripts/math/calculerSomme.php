<?php
function calculerSomme($nombres)
{
    $sum = 0;
    $valid_nbr = [];
    foreach ($nombres as $nbr) {

        if (is_int($nbr) || is_float($nbr)) {
            $sum += $nbr;
            $valid_nbr[] = $nbr;
        }
    }
    return [$sum, $valid_nbr];
}
