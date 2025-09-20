using System;
using System.Reflection.Metadata;

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
        for (int i = 0; i < 100; i++)
        {
            Exercices.Ex10(Exercices.GetValidBBAN());
        }
        Exercices.Ex13();
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
}


