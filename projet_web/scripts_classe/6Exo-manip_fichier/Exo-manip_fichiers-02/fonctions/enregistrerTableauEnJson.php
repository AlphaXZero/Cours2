<?php
function enregistrerTableauEnJson($filename, $array)
{
    file_put_contents(
        $filename,
        json_encode($array)
    );
}
