<?php
function genererSuiteFibonacci($n)
{
    if ($n == 0) {
        return 0;
    }
    if ($n == 1) {
        return 1;
    }
    return genererSuiteFibonacci($n - 1) + genererSuiteFibonacci($n - 2);
}

function creerListeNFib($n)
{
    for ($i = 0; $i <= $n; $i++) {
        echo ("$i -> " . genererSuiteFibonacci($i) . PHP_EOL);
    }
}
creerListeNFib(9);
