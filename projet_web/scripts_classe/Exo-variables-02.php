<?php
$claudyVousDitBonjour = 'coucou petite perruche !' . PHP_EOL;
#1
$claudyVousDitAurevoir = str_replace("coucou","aurevoir", $claudyVousDitBonjour);
echo $claudyVousDitAurevoir;
#2
$claudyVousDitBonjour = ucfirst($claudyVousDitBonjour);
echo $claudyVousDitBonjour;
#3
$claudyVousDitBonjour = strtoupper($claudyVousDitBonjour);
echo $claudyVousDitBonjour;