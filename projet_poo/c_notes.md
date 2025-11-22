# 📚 Notes C# - Récapitulatif

## 🧱 Commandes .NET CLI

```bash
dotnet new console -n NOM        # Créer un nouveau projet console
dotnet run                       # Exécuter l'application
````

* `.sln` : Fichier solution (contient les projets)
* `.csproj` : Fichier de configuration du projet (dépendances, etc.)
* `/bin` : Fichiers finaux compilés
* `/obj` : Fichiers temporaires de build

---

## 🖨️ Affichage Console

```csharp
Console.WriteLine();             // Affiche avec saut de ligne
Console.Write();                 // Affiche sans saut de ligne
Console.ReadLine();             // Lire une entrée utilisateur
```

### Interpolation de chaînes

```csharp
$"{variable}"                    // Interpolation
```

---

## 🔢 Variables & Types

Types :

```csharp
int, char, bool, string, const, long, float, double, byte, decimal
```

* `int?` ou `Nullable<int>` : permet une valeur nulle
* `var` : déduction automatique du type
* `value = oui ?? non;` : opérateur de coalescence nulle
* `(int) 3` ou `3 as int?` : cast explicite
* `int.MinValue`, `int.MaxValue` : bornes

### Mémoire

* **Valeurs** (types primitifs) : stockés sur le **stack**
* **Références** (objets, classes) : stockés sur le **heap**

### Divers

```csharp
34.ToString("00")               // Format à 2 chiffres
```

---

## 🧮 Fonctions & Méthodes

Déclaration :

```csharp
class MaClasse {
    public static void MaMéthode() { }
}
MaClasse.MaMéthode();
```

Fonctions fléchées :

```csharp
int Additionner(int a, int b) => a + b;
```

Params :

```csharp
int Add(params int[] nombres) { ... }
```

Surcharge :

```csharp
int Additionner(int a, int b)
float Additionner(float a, float b)
```

---

## 🧠 Conditions

```csharp
if (condition) {
} else if (condition) {
} else {
}
```

Opérateurs :

* `||` : OU
* `&&` : ET

Switch :

```csharp
switch (var) {
    case "potato":
    case "apple":
        // instructions
        break;
    default:
        // instructions
        break;
}
```

---

## 🔁 Boucles

```csharp
for (int i = 0; i < 10; i++) { }

while (condition) { }

do {
} while (condition);

foreach (var item in collection) { }
```

---

## 🧰 Méthodes Utiles

```csharp
Math.Round(var, 2);                // Arrondir à 2 décimales
if (n is string) { }              // Vérifie le type
typeof(variable);                 // Type statique
objet.GetType();                  // Type dynamique
type.Parse(var);                  // Conversion
type.TryParse(var, out valeur);  // Conversion sécurisée
Convert.ToInt32(valeur);         // Conversion
string.Contains("mot");          // Contient ?
str.Trim();                       // Supprime les espaces
string.IndexOf(".");             // Index d'un caractère
```

---

## 📚 Tableaux & Collections

### Tableaux

```csharp
string[] tableau = new string[3];
string[] noms = { "oui", "non" };
int[,] tab = new int[10, 11];

foreach (string nom in noms) { }

String.Join(", ", noms);          // Concaténation
```

Plages (ranges) :

```csharp
[1..^1]   // du 2e au dernier exclu
[0..5]    // des index 0 à 4
```

### Listes

```csharp
var maListe = new ArrayList();
var maListeTyped = new List<int>();
var maListtyped = new List<int>{1,2,3};
maListeTyped.Add(1);
maliste.count()
```

### Dictionnaires

```csharp
var maHashtable = new Hashtable();
maHashtable["clé"] = 43;

foreach (DictionaryEntry entry in maHashtable) { }

var monDico = new Dictionary<string, int>();
monDico.ContainsKey(number) //return bool
monDico.Add("xxxx",45)
mondico.Remove("xxx")
Accounts.Keys 
Account.Values
```

---

## 🏗️ Structures

```csharp
struct Point {
    public int X;
    public int Y;

    public Point(int t) {
        X = t;
        Y = 0;
    }

    public override string ToString() {
        return $"X: {X}, Y: {Y}";
    }
}

Point point = new Point(10);
point.X = 5;
```

* Différence avec une classe : **structure = type valeur** (plus léger, pas de polymorphisme)

---

## 🚗 Énumérations

```csharp
enum Carburant { Essence, Diesel, Gaz, Elec }

Carburant type = Carburant.Essence;
```

---

## 👤 Classes

Déclaration simple :

```csharp
class Personne {
    public string Nom;
    public string Prenom;
}
```

Constructeur :

```csharp
class Personne {
    public string Nom;
    public string Prenom;

    public Personne(string nom, string prenom) {
        Nom = nom;
        Prenom = prenom;
    }
}
```

### `partial` classes

Permet de séparer une classe sur plusieurs fichiers :

```csharp
partial class Person {
    int a = 1;
}

partial class Person {
    int b = 2;
}
```

### Classe `static`

```csharp
static class Exemple {
    public static int Compteur = 0;
}
```

* Non instanciable, uniquement des membres statiques.

---

## Namespaces
```csharp
using system; # mtn c sharp le fait tout seul
namespace Cours{
    class Program{
        static void Main(string[] args){
            system.console.writeline
        }
    }
}
```
using permet d'import
 
### Encapsulation
voiture     
-Moteur - = privé    
+DemarerVoiture() + = public

- public parout
- protected classe + enfants
- private classe
- internal accessicible ds projet

### getter et setter
```csharp
public class Personne
{
private int age;
public int Age
{
get{return age;}
set{age=value;}
}
}```
 //ou
public int Age{get;set;}
```
## héritage
```csharp
class person{
    age=
}
class person: etudiant{
    etudes=
}
```

### override
```csharp
public override void ToString(){}
```

### base
```csharp
class oui(){
    se presenter()
}
class oui.non(){
    base.se presenter()
}
```
- private la classe
- protected la classe et ses enfants
- public partout
 ### sealed 
 pour empêcher héritage

## Classes abstraites
```csharp
abstract class

```

# Interface
commencer par un I maj
```csharp
public interface Idessinable{
    void dessiner()
}
public class Cercle : Idessinable{
    public void dessiner()
}
```

## garbage collector
faire interface IDsisposable 
```csharp
class Exemple : IDisposable{
    public void Dispose(){
        //liberer les ressources ici
    }
}
```

# Constructeurs
même non que classes sans type de retour 
```csharp
class Personne{
    puclic Personne(){

    }
}
```
on peut mettre plusieurs constructeurs ds 1 même classe
public person(string nom, string prenom)
public person(int age)

# Exceptions 
```csharp
try{
    throw new NotimplentedException('En cours de dev')
}
cathc(Exception ex){
    console.WriteLine(ex.Message);
    throw;
}

try {
    10/0
}
catch(DivididedByZeroException ex)
catch(Exception ex)
finaly{}


```

# délégués
liste chainés de pointeurs typés de fonction
classe Delegate
```csharp
MyDelegate md = MyMethod
void MyMethod()=Constole.write(hello)
delegate void MyDelegate();
```
on peut ajouter des méthode ou supprimer avec -= ou +=

# évenements
