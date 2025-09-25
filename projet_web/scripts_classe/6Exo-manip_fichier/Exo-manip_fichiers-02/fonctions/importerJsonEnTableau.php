<?php
function importerJsonEnTableau($filename)
{
    return json_decode(file_get_contents($filename), true);
}
