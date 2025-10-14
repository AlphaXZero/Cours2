using System;
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.Design;
using System.Diagnostics.CodeAnalysis;
using System.Diagnostics.Metrics;
using System.Drawing;
using System.Reflection.Metadata;
using BenchmarkDotNet.Disassemblers;
using Bibliotheque;
using Utilisateurs;

class Program
{
    static void Main(string[] args)
    {
        // Exercices.Ex1();
        // Exercices.Ex2();
        // Exercices.Ex3();
        // Exercices.Ex4();
        // Exercices.Ex5();
        // Exercices.Ex6();
        // Exercices.Ex7();
        // Exercices.Ex8();
        // Exercices.Ex9();

        // Exercices.Ex10(Exercices.GetValidBBAN());

        // Console.WriteLine(Exercices.Ex18("hautuah"));
        // Console.WriteLine(Exercices.Ex19(20));
        // Exercices.Ex21();
        // Celsius temp = new Celsius(20);
        // Console.WriteLine($"{temp.temperature} => {temp.convertir().temperature}");
        Voiture lamienne = new(100, 0, new("V6", 6), new List<Roue> { new(20), new(10) });
        Conducteur pierre = new("Pierre", lamienne);
        pierre.Conduire();
        pierre.Accelerer(20);
        pierre.Conduire();
        lamienne.AfficherDetails();

        // Livre oui = new("mobydick", "jean de la fontaine", 1999);
        // Livre non = new("1986", "Tchernobyl", 1987);
        // Livre non2 = new("2001", "infini", 2042);
        // Etudiant jean = new("Pierre", "Marc", new List<Livre> { oui, non });
        // jean.AfficherInfo();
        // jean.Livres.Add(non2);
        // jean.AfficherInfo();
    }
}
class Exercices
{
    public static void Ex1()
    {
        Console.WriteLine("Nom ?");
        string? name = Console.ReadLine();
        Console.WriteLine("Age ?");
        string? age = Console.ReadLine();
        Console.WriteLine("Vous êtes " + name + " et vous avez " + age);
    }
    public static void Ex2()
    {
        int a = 2;
        int b = 4;
        Console.WriteLine($"somme : {a + b} produit : {a * b} quotient : {a / b}");
    }
    public static void Ex3()
    {
        Console.WriteLine("Entrez une valeur décimale");
        string? usr_input = Console.ReadLine();
        double val = double.Parse(usr_input);
        Console.WriteLine($"la valeur arrondie est {Math.Round(val, 2)}");
    }
    public static void Ex4()
    {
        int day_amount = 123;
        Console.WriteLine($"{day_amount} jours font {day_amount * 24} heures soit {day_amount * 24 * 60} minutes ou {day_amount * 24 * 60 * 60} secondes");

    }

    public static void Ex5()
    {
        Console.WriteLine("Entrez un nombre à doubler");
        Console.WriteLine(int.TryParse(Console.ReadLine(), out int nbrToDouble) ? nbrToDouble * 2 : "Entrée invalide");
    }

    public static void Ex6()
    {
        Console.WriteLine("Entrez un nombre décimal");
        Console.WriteLine(float.TryParse(Console.ReadLine(), out float decimalNbr) ? Convert.ToInt32(decimalNbr) : "Entrée invalide");
    }

    public static void Ex7()
    {
        int celTemp = 20;
        Console.WriteLine($"{celTemp}°C fait {celTemp * (float)9 / (float)5 + 32}° en Fahrenheit");
    }

    public static void Ex8()
    {
        if (!int.TryParse(Console.ReadLine(), out int Nbr))
        { Console.WriteLine("Entrée invalide"); }
        else
        {
            Console.WriteLine(Nbr % 2 == 0 ? "Le nombre est pair" : "Le nombre est impair");

        }
    }

    public static void Ex9()
    {
        Console.WriteLine("Entre 2 nombres");
        if (int.TryParse(Console.ReadLine(), out int Nbr1) && int.TryParse(Console.ReadLine(), out int Nbr2))
        {
            Console.WriteLine("Entre une opération +,*,- ou /");
            var op = Console.ReadLine();
            int? output = null;
            switch (op)
            {
                case "+":
                    output = Nbr1 + Nbr2;
                    break;
                case "-":
                    output = Nbr1 - Nbr2;
                    break;
                case "/":
                    output = Nbr2 == 0 ? Nbr1 / Nbr2 : null;
                    break;
                case "*":
                    output = Nbr1 * Nbr2;
                    break;
                default:
                    Console.WriteLine("Opération non reconnue");
                    break;
            }
            Console.WriteLine(output != null ? $"{Nbr1} {op} {Nbr2} = {output}" : "opération invalide");
        }
    }

    public static void Ex10(string BBAN)
    {
        var firstTen = double.Parse(BBAN[0..10]);
        var lastTwo = int.Parse(BBAN[^2..]);
        Console.WriteLine((firstTen % 97 == lastTwo) || (firstTen % 97 == 0 && lastTwo == 97) ? $"{BBAN} valide" : $"{BBAN} invalide");
    }

    public static string GetValidBBAN()
    {
        int[] oui = new int[10];
        Random rdn = new Random();
        for (int i = 0; i < 10; i++)
        {
            oui[i] = rdn.Next(10);
        }
        var partie1 = String.Join("", oui);
        var nombre = long.Parse(partie1);
        var bban = partie1 + (nombre % 97 != 0 ? (nombre % 97).ToString("00") : "97");
        return bban;

    }
    public static void Ex11()
    {
        int sum = 0;
        for (int i = 2; i <= 100; i += 2)
        {
            sum += i;
        }
        Console.WriteLine(sum);
    }
    public static void Ex12()
    {
        Console.WriteLine("Entrez un nombre pour avoir sa factorielle");
        Console.WriteLine(int.TryParse(Console.ReadLine(), out int nbr2) ? "" : "Entrée invalide");
        int fact = 1;
        while (nbr2 > 0)
        {
            fact *= nbr2;
            nbr2 -= 1;
        }
        Console.WriteLine(fact);

    }

    public static void Ex13()
    {
        Console.WriteLine("Entrez un nombre pour avoir sa table de mult");
        Console.WriteLine(int.TryParse(Console.ReadLine(), out int nbr2) ? "" : "Entrée invalide");
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{i} x {nbr2} = {i * nbr2}");
        }
    }

    public static void Ex14()
    {
        int[] tab = [10, 0, 10, 0];
        int sum = 0;
        foreach (int i in tab)
        {
            sum += i;
        }
        Console.WriteLine($"somme : {sum}, moyenne : {(float)sum / (float)tab.Length}");
    }

    public static void Ex15()
    {
        int[] tab = [10, 0, 10, 0];
        int min = 10000000;
        int max = -10000000;
        foreach (int i in tab)
        {
            min = i < min ? i : min;
            max = i > max ? i : max;
        }
        Console.WriteLine($"min : {min}, max : {max}");
    }
    public static void Ex16()
    {
        int[,] tab = new int[10, 10];
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                tab[i, j] = (i * 10) + (j + 1);
                Console.Write($"{tab[i, j].ToString("00")} ");
            }
            Console.WriteLine();
        }
    }
    public static int Ex17(int a)
    {
        int sum = 0;
        for (int i = 2; i <= a; i += 2)
        {
            sum += i;
        }
        return sum;
    }
    public static bool Ex18(string oui)
    {
        return oui == String.Join("", oui.Reverse());
    }
    public static float Ex19(int celTemp)
    {
        return (float)9 / (float)5 + 32;
    }
    public static void Ex20()
    {
        var primeNumber = new List<int>();
        Console.WriteLine("Entrez un nombre");
        var user_input = Console.ReadLine();
        int counter = 2;
        while (counter < int.Parse(user_input))
        {
            if (isPrime(counter))
            {
                primeNumber.Add(counter);
            }
            counter += 1;
        }
        Console.WriteLine(string.Join(" ", primeNumber));
    }


    public static void Ex21()
    {
        var primeNumber = new List<int>();
        Console.WriteLine("Entrez un nombre");
        var user_input = Console.ReadLine();
        for (int i = 2; primeNumber.Count < int.Parse(user_input); i++)
        {
            if (isPrime(i))
            {
                primeNumber.Add(i);
            }
        }
        Console.WriteLine(string.Join(" ", primeNumber));
    }
    public static bool isPrime(int n)
    {
        for (int i = 2; i <= (int)Math.Sqrt(n); i++)
        {
            Console.WriteLine(i);
            if (n % i == 0)
            {
                return false;
            }
        }
        return true;
    }
}


struct Celsius
{
    public double temperature;
    public Celsius(double temp)
    {
        temperature = temp;
    }
    public Fahrenheit convertir()
    {
        return new Fahrenheit(temperature * 9 / 5 + 32);
    }
}
struct Fahrenheit
{
    public double temperature;
    public Fahrenheit(double temp)
    {
        temperature = temp;
    }
    public Celsius convertir()
    {
        return new Celsius((temperature - 32) * 5 / 9);
    }
}

enum Marques
{
    Mercedes, BMW
}
enum Vitre
{
    Teinte, Blanc
}
struct Voiturette
{
    public int vitesse;
    public Marques marque;
    public Voiturette(int vit, Marques marq)
    {
        vitesse = vit;
        marque = marq;
    }
    public void accelerer(int accel)
    {
        vitesse += accel;
    }
    public override string ToString()
    {
        return $"la voiture {marque} roule à {vitesse}";
    }
}

class Voiture(int vitesse, Marques marque, Moteur moteur, List<Roue> roue)
{
    public int Vitesse = vitesse;
    public Marques Marque = marque;
    public Moteur Moteur = moteur;
    public List<Roue> Roue = roue;
    public void Accelerer(int accel)
    {
        Vitesse += accel;
    }
    public void AfficherDetails()
    {
        Console.WriteLine($"possède un {Moteur.Modele} de {Moteur.Cylindre} cylindres et possède {Roue.Count()} roues : ({String.Join(", ", Roue.Select(n => n.ToString()))})");
    }
    public override string ToString()
    {
        return $"la voiture {Marque} roule à {Vitesse}";
    }
}

class Chat(string couleur, string nom, int age)
{
    public string Couleur = couleur;
    public string Nom = nom;
    public int Age = age;
    public void miauler()
    {
        Console.WriteLine("miaouuu");
    }
    public void vieillir(int annee)
    {
        Age += 1;
    }
}

class Conducteur(string nom, Voiture voiture)
{
    public string Nom = nom;
    public Voiture Voiture = voiture;

    public void Conduire()
    {
        Console.WriteLine($"{Nom} conduit. {Voiture}");
    }

    public void Accelerer(int valeur)
    {
        Voiture.Accelerer(valeur);
    }
}

class Moteur(string modele, int cylindre)
{
    public string Modele = modele;
    public int Cylindre = cylindre;
}

class Roue(int pouces)
{
    public int Pouces = pouces;
    public override string ToString()
    {
        return $"Roue de {pouces}";
    }
}


