<?php
function afficherElementsFichier($fileName)
{
    echo (file_get_contents("./" . $fileName));
}
