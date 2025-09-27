<?php
const ALPHA_RANGE = "abcdefghijklmnopqrstuvwxyz";
const MAX_LIVES = 6;

function get_user_letter(array $used_letters): string
{
    while (true) {
        $user_input = strtolower(readline("Proposez une lettre : "));
        if (
            mb_strlen($user_input) > 1
            || !str_contains(ALPHA_RANGE, $user_input)
            || in_array($user_input, $used_letters)
        ) {
            echo "Veuillez ne rentrer qu'une seule lettre valide !\n\n";
        } else {
            echo PHP_EOL;
            return $user_input;
        }
    }
}


function get_random_word(string $category): string
{
    $words_dict = json_decode(file_get_contents("./data/dictionnaire.json", true));

    switch ($category) {
        case 'nourriture':
            $words_array = $words_dict->nourriture;
            break;
        case 'animaux':
            $words_array = $words_dict->animaux;
            break;
        case 'professions':
            $words_array = $words_dict->professions;
            break;
        case 'sciences':
            $words_array = $words_dict->sciences;
            break;
        case 'all':
        default:
            $words_array = array_merge(
                $words_dict->nourriture,
                $words_dict->animaux,
                $words_dict->professions,
                $words_dict->sciences
            );
            break;
    }

    return $words_array[array_rand($words_array)];
}

function format_revealed_letters(array $revealed_letters): string
{
    return implode("", $revealed_letters);
}

function format_used_letters(array $used_letters): string
{
    return "[" . implode(" ", $used_letters) . "]";
}

function update_revealed_letter(string $target_word, array $revealed_letters, string $user_input): array
{
    if (str_contains($target_word, $user_input)) {
        foreach (str_split($target_word) as $i => $char) {
            if ($char === $user_input) {
                $revealed_letters[$i] = $char;
            }
        }
    }
    return $revealed_letters;
}

function is_win(array $revealed_letters, string $target_word): bool
{
    return implode("", $revealed_letters) === $target_word;
}

/**
 * Start a game of "pendu"
 * @param string $category The word category to use. Possible values are:
 *                         'nourriture', 'animaux', 'professions', 'sciences', or 'all'.
 *                         Defaults to 'all'.
 *
 * @return void
 */
function do_game($category = "all"): void
{
    $remaining_life = MAX_LIVES;
    $used_letters = [];
    $target_word = get_random_word($category);
    $revealed_letters = array_fill(0, mb_strlen($target_word), "-");

    echo "Bienvenue dans le jeu du pendu !" . PHP_EOL . PHP_EOL;

    while (true) {
        echo "-----------------------------\n";
        echo "Vies restantes : $remaining_life" . PHP_EOL;
        echo "Lettres proposées : " . format_used_letters($used_letters) . PHP_EOL;
        echo "Mot : " . format_revealed_letters($revealed_letters) . PHP_EOL . PHP_EOL;

        $letter_choice = get_user_letter($used_letters);
        $used_letters[] = $letter_choice;

        $initial_guess = $revealed_letters;
        $revealed_letters = update_revealed_letter($target_word, $revealed_letters, $letter_choice);

        if ($initial_guess === $revealed_letters) {
            echo "La lettre $letter_choice ne se trouve pas dans le mot mystère !\n\n";
            $remaining_life--;
        } else {
            echo "La lettre $letter_choice se trouve dans le mot mystère !\n\n";
        }

        if (is_win($revealed_letters, $target_word)) {
            echo "Le mot était bien : $target_word\n";
            echo "Félicitations, vous avez gagné !\n";
            break;
        } elseif ($remaining_life <= 0) {
            echo "Le mot était : $target_word\n";
            echo "Dommage, vous avez perdu !\n";
            break;
        }
    }
}
