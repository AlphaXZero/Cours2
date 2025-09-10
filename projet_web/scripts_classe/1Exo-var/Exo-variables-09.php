<?php
$listeDeFilmsParCategorie = [
    'scienceFiction' => [
        ['nomDuFilm' => 'Blade Runner 2049', 'realisateur' => 'Denis Villeneuve', 'annee' => 2017],
        ['nomDuFilm' => 'Dune', 'realisateur' => 'Denis Villeneuve', 'annee' => 2021],
        ['nomDuFilm' => 'Minority Report', 'realisateur' => 'Steven Spielberg', 'annee' => 2002]
    ],
    'horreur' => [
        ['nomDuFilm' => 'Hellraiser', 'realisateur' => 'Clive Barker', 'annee' => 1987],
        ['nomDuFilm' => 'La colline a des yeux', 'realisateur' => 'Alexandre Aja', 'annee' => 2006]
    ],
    'comedie' => [['nomDuFilm' => 'Dikkenek', 'realisateur' => 'Olivier van', 'annee' => 2006]]
];
unset($listeDeFilmsParCategorie['comedie'][0]['annee']);
print_r($listeDeFilmsParCategorie);
$listeDeFilmsParCategorie['scienceFiction'] = array_values($listeDeFilmsParCategorie['scienceFiction']);
print_r($listeDeFilmsParCategorie);
