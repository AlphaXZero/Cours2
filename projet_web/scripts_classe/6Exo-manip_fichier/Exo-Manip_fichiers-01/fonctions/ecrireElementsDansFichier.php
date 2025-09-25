<?php
function ecrireElementsDansFichier($fileName, $arraySentence)
{
    $content = file_get_contents($fileName);
    foreach ($arraySentence as $sentence) {

        $content .= $sentence . PHP_EOL;
    }
    file_put_contents("./" . $fileName, $content);
}
