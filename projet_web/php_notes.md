
# Notes PHP — Récapitulatif Complet

IMPORTANT POUR APACHE:
sudo micro /etc/apache2/sites-enabled/cookie.t*
```bash
<VirtualHost *:80>
    ServerName oui.test
    ServerAlias localhost
    DocumentRoot /var/www/html/modules

    <Directory /var/www/html/modules>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/oui_error.log
    CustomLog ${APACHE_LOG_DIR}/oui_access.log combined
</VirtualHost>
```
sudo micro /etc/hosts
et ajouter une ligne 127.0.0.s1 <le_nom.test>

---

## Strings

```php
echo " {$var}";                         // Interpolation
echo $prenom . $nom;                    // Concaténation
$var .= "oui";                          // Ajout à une chaîne existante
$var = str_replace($search, $replace, $var);  // Remplacer une chaîne
$var = ucfirst($var);                  // Mettre la première lettre en majuscule
$var = strtoupper($var);              // Tout en majuscule
trim($str);                            // Supprimer espaces (comme strip())
str_contains($string, $substring);    // Vérifie si une chaîne contient une autre
```

## Int

```php
$non += 1;                              // Incrémentation
is_int($var);                           // Vérifie si entier
is_float($var);                         // Vérifie si flottant
is_numeric($var);                       // Vérifie si nombre
round($valeur, 2);                      // Arrondir
rand(1, 20);                            // Nombre aléatoire
```

---

## Types et Debug

```php
gettype($var);                          // Type de la variable
var_dump($var);                         // Affiche type + contenu
print_r($arr);                          // Affiche une liste lisible
empty($var);                            // Est vide ?
isset($var);                            // Est définie ?
```

---

## Arrays

### Manipulation

```php
$var = [];                              // Créer un tableau
$var[] = 'oui';                         // Ajouter à la fin
unset($var[0]);                         // Supprimer un élément
$var = array_values($var);             // Réindexer
array_merge($arr1, $arr2);             // Fusionner
array_diff($arr1, $arr2);              // Différence
array_sum($arr);                       // Somme des éléments
array_rand($arr);                      // Élement aléatoire
in_array("str", $arr);                 // Contient ?
array_search("str", $arr);            // Cherche une valeur
implode(",", $arr);                    // Convertir en chaîne
count($arr);                           // Nombre d’éléments
array_key_exists("clé", $arr);         // Clé existe ?
```

### Tableaux associatifs

```php
$var = ['age' => 2, 'name' => 'Jean-Eude'];
echo $var['age'];                      // Accès à la valeur
```

### Tri

```php
asort($arr);                           // Ascendant (conserve les clés)
arsort($arr);                          // Descendant (conserve les clés)
sort($arr);                            // Ascendant (réindexe)
uasort($arr, fn($a, $b) => $a <=> $b); // Tri personnalisé
```

---

## Conditions

```php
if ($var >= 5) {
    // ...
} elseif (...) {
    // ...
} else {
    // ...
}

$var = $var2 ?? 'valeur par défaut';  // Null coalescing
$condition ? 'vrai' : 'faux';        // Ternaire

switch($var) {
    case 0:
        echo 'zéro';
        break;
    default:
        echo 'autre';
}
```

---

## Boucles

### While

```php
while ($var > 3) {
    $var++;
}
```

### For

```php
for ($i = 1; $i < 6; $i++) {
    echo $i;
}
```

### Foreach

```php
$tab = ['Claude', 'Jean'];
foreach ($tab as $value) {
    echo $value;
}

// Avec index :
foreach ($tab as $index => $value) {
    echo "$index : $value";
}
```

---

## Fonctions

```php
function faireOui(int $oui): void {
    echo $oui;
}
```

* Paramètres optionnels : `...$args` (splat operator)
* Décompression tableau :

```php
$valeurs = [2, 3];
afficherSomme(...$valeurs);
```

---

## 🔁 Fonctions sur tableaux

### `array_map()`

```php
array_map('faireOui', $nombres);

array_map(function($val) {
    return $val * 2;
}, $nombres);

// Arrow function
array_map(fn($val) => $val * 2, $nombres);
```

### `array_filter()`

```php
$nombresImpairs = array_filter($nombres, fn($n) => $n % 2 !== 0);
```

### `array_reduce()`

```php
$somme = array_reduce($nombres, fn($acc, $n) => $acc + $n, 0);
```

### `usort()`

```php
$mots = ["Jean-Luc", "Claude", "Bob"];
usort($mots, fn($a, $b) => mb_strlen($a) - mb_strlen($b));
```

---

## PHPDoc (Documentation)

```php
/**
 * Calcule et affiche le double d'une valeur entière ou flottante.
 *
 * @param float $valeur La valeur devant être doublée.
 * @return void
 */
```

---

## Inclusion de fichiers

```php
include 'fichier.php';         // Continue en cas d'erreur
require 'fichier.php';         // Erreur fatale
require_once 'fichier.php';    // Une seule inclusion
require_once __DIR__ . DIRECTORY_SEPARATOR . 'fichier.php';
```

---

## 📁 Fichiers

### Lire un fichier

```php
$monFichier = fopen($chemin, "r");
while (!feof($monFichier)) {
    $ligne = fgets($monFichier);
}
fclose($monFichier);
```

### Lire rapidement

```php
$contenu = fread($monFichier, filesize($chemin));
```

### Écrire dans un fichier

```php
$monFichier = fopen($chemin, "w");
fwrite($monFichier, "Texte");
fclose($monFichier);
```

### Remettre le pointeur au début

```php
fseek($monFichier, 0);
```

### Supprimer un fichier

```php
unlink(__DIR__ . DIRECTORY_SEPARATOR . 'fichier.txt');
```

### Verrouillage (exclusif)

```php
if (flock($monFichier, LOCK_EX)) {
    fwrite($monFichier, "Ligne");
    flock($monFichier, LOCK_UN);
}
```

### Alternative simplifiée

```php
$contenu = file_get_contents(__DIR__ . '/fichier.txt');
$contenu .= "Nouvelle ligne\n";
file_put_contents(__DIR__ . '/fichier.txt', $contenu, LOCK_EX);
```

---

## JSON

```php
$chemin = __DIR__ . '/exemple.json';
$contenuJSON = file_get_contents($chemin);
$data = json_decode($contenuJSON, true);
$dataModifie = json_encode($data, JSON_PRETTY_PRINT);
file_put_contents($chemin, $dataModifie);
```

---

## Fonctions système / fichiers

```php
if (file_exists($chemin)) {
    echo "$chemin existe !";
}

is_dir($chemin);
scandir($chemin);              // Liste des fichiers/dossiers
```

---

## Entrées utilisateur

```php
$var = readline('Votre nom : ');
```

---

## Validation d’email

```php
filter_var($email, FILTER_VALIDATE_EMAIL);
```

---

# Pages dynamiques avec php 
## base
```php
<?php require_once __DIR__ . DIRECTORY_SEPARATOR . 'header.php'; ?>
<h2>Bienvenue sur votre site web !</h2>
```
## variable php dans html

```php
<?php
$metaDescription = "description de la page actuelle...";
require_once __DIR__ . DIRECTORY_SEPARATOR . 'header.php';
?>// dans index.php
```
```html
dans header.php
<head> 
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="<?=$metaDescription ?? ""?>">
    <title>Mon Premier Modèle de Page Dynamique</title>
</head>
```
\<?=$var> == <?php echo "$var">

## Formulaires

 ```html
 <form action="/action_page.php">
  <input type ="hidden" name="formName" value="form01">
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
  <button type="submit" >oui</button>
</form> 
 ```
method =    
get -> affiche en haut     
psot -> n'affiche pas en haut

Pour récup : 
```php
<?php     
var_dump($_get/$_post) 
```

Pour tester post:
```php
if ($_DERVER['Request_Method']== 'POST'){
    var_dump($_post["prenom"])
}
```

NE PAS FAIRE CONFIANCE A USER
Meilleur option: (peut-mettre $regle dans autre dossier)
```php
<?php
function nettoyerEntreeUtilisateur(array $entreesUtilisateur, string $nomChamp): string
{
    return trim($entreesUtilisateur[$nomChamp] ?? '');
}

function estRempli(string $entreeUtilisateur): bool
{
    return $entreeUtilisateur != '';
}

function respecteLongueurMinEtMax(string $entreeUtilisateur, int $longueurMin, int $longueurMax): bool
{
    return mb_strlen($entreeUtilisateur) >= $longueurMin
        && mb_strlen($entreeUtilisateur) <= $longueurMax;
}

function verifierValiditeChamps(array $reglesDesChamps, array $entreesUtilisateur): array
{
    $erreurs = [];

    // Accéder à toutes les règles de chaque champ :
    foreach ($reglesDesChamps as $nomDuchamp => $reglesDuChamp)
    {
        $valeurDuChamp = nettoyerEntreeUtilisateur($entreesUtilisateur, $nomDuchamp);

        // Si le champ est vide :
        if (!estRempli($valeurDuChamp))
        {
            // Stocker le message d'erreur approprié si le champ est REQUIS :
            if (
                isset($reglesDuChamp['requis'])
                && $reglesDuChamp['requis'] === true
            )
            {
                $erreurs[$nomDuchamp] = '<p>Ce champ est requis!</p>';
            }
        }
        else
        {
            if (
                isset($reglesDuChamp['longueurMin'])
                && isset($reglesDuChamp['longueurMax'])
                && !respecteLongueurMinEtMax($valeurDuChamp, $reglesDuChamp['longueurMin'], $reglesDuChamp['longueurMax'])
            )
            {
                $erreurs[$nomDuchamp] = "<p>Ce champ doit comprendre entre {$reglesDuChamp['longueurMin']} et {$reglesDuChamp['longueurMax']} caractères!</p>";
            }
        }
    }

    return $erreurs;
}

if ($_SERVER["REQUEST_METHOD"] === "POST")
{
    $reglesDesChamps = [
        'nom' => [
            'requis' => true,
            'longueurMin' => 2,
            'longueurMax' => 255
        ],
        'prenom' => [
            'longueurMin' => 2,
            'longueurMax' => 255
        ],
        'message' => [
            'requis' => true,
            'longueurMin' => 10,
            'longueurMax' => 3000
      ]
    ];

    $erreurs = verifierValiditeChamps($reglesDesChamps, $_POST);

    // S'il n'y a aucune erreur, stocker le message de validation du formulaire :
    if (empty($erreurs))
    {
        $formMessage = "<p>Formulaire envoyé avec succès!</p>";
    }
}
?>

```

# Errors
lever une exception :
```php
try{
    throw new Exception("oiu")
}
catch (Exception $e){
    echo "$e->getMessage()"
}


$t instanceof Exception
getTrace()
```

# BDD
```php
il faut décrire des trucs avec $dsn
$dsn ="mysql:host=$nomDuServeur;dbname=$nomBDD;charset=utf8mb4"

$pdo = new PDO($dsn, $utilisateur, $mdp)

$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO;;ERRMODE_EXCEPTION)

catch(PDOException $e){
    echo "Erreur d'éxec de requète :{$e->getMessage()}";
}

$pdo = null; pour libérer bdd
```

```php
$pdo->exec($requete);

$rqst = "select * from t_utis"
$stmt= $pdo->query($rqst);

$util= $stmt->fetchall(PDO::FETCH_ASSOX) pour un dictionnaire
if ($util){

}

```

where email =:email

$stmt->bindValue(":email",$email,PDO::PARAM_STR)
$stm->execute();
$utilisateur = $dm->fetch(PDO::FETCH_ASSOC)

insert into t_commentaire_com (com_auteur,com_contenu)

---
 
# Cookies
setcookie(
    string $name,
    string $value = "",
    array $options = [
        'expires' => 0,
        'path' => "",           // Par défaut, le chemin de la page courante.
        'domain' => "",         // Par défaut, le domaine de la page courante.
        'secure' => false,
        'httponly' => false,
        'samesite' => ''        // Par défaut, comportement par défaut du navigateur.
    ]
): bool
samesite : - strict : si on change de domaine pas envoyer
           - lax : accepte que cookier soi envoyer même si autre domaine mais seulement si provient d'un lien
           - none : cookie envoyé ds ttes les requetes
-> httponly et secure en true
```php
$expiration = time() + 60*24*60
setcookie('nom','val',['expires'=>$expiration])

#lire
$cook = $_COOKIE['nomducookie'];
```

## Variables de session

lancer 
session_start();

$_Session['utilisatuer_id'] = 5;
if isset($_Session['utilisateur_id'])

# Regex
preg_match($regex,$texte) renvoie true false
on peut mettre aussi $match en param pour avoir une liste



# host virtual
sudo nano /etc/apache2/sites-available/html.test.conf
<VirtualHost *:80>
    ServerName html.test
    DocumentRoot /var/www/html

    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/html_error.log
    CustomLog ${APACHE_LOG_DIR}/html_access.log combined
</VirtualHost>

puis activer :
sudo a2ensite html.test.conf
sudo systemctl reload apache2

# js
var = global 
let = mieux si veut pas global

script src="" defer télécharge totu
async tout en parrallel mais respecte pas ordre 

export depuis un fichier à la fin pour mettre dans le module (voir cours)
il faut import ensuite en mettant le chemin

## events
on sélectionne un élément
const bouton = document.querySelector('button')
bouton.onclick = function(){}

+Propre:
element.addEventListener(type(click,mouseover,keydown,input,scroll,...), fonction à appeller)
supprimer
element.removeEventListener('click',fonction)

-objet event
const button = documenet.query
const gereClick= (event)=>{
    console.long("element courant de levent: ${event.currentTarget.id})
}

-recup positoin souris
const gereMouse =(event)=>
{
    const x = event.clientx
    const y = event.clienty
}
window.addeEventListner('mousemove',geremouse)
window=la fenetre

- recup texte dans formulaire 
const monInput = doc.querey
nomInput.value

pour checkbox
oui.checked

valueAsNumber pour avoir un nombre
valueAsDate

# classes gestion
pour ajouter une classe get element avant

ampoul.classList.toggle("alerte")
pour savoir si elle fait partie de la classe
ampoul.classList.contains("alerte")

ne pas utilise sauf cas particulier ex : truc sur la souris
ampoule.style.backgroundColor = "green"