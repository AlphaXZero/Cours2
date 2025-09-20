using System;

class Program
{
    static void Main(string[] args)
    {
        // Exercice1.Run();
        // Exercice2.Run();
        // Exercice3.Run();
        // Exercice4.Run();
        // Exercice5.Run();
        // Exercice6.Run();
        // Exercice7.Run();
        // Exercice8.Run();
        // Exercice9.Run();
        Exercice10.Run();
    }
}

class Exercice1
{
    public static void Run()
    {
        Console.WriteLine("Nom ?");
        string? name = Console.ReadLine();
        Console.WriteLine("Age ?");
        string? age = Console.ReadLine();
        Console.WriteLine("Vous êtes " + name + " et vous avez " + age);
    }
}

class Exercice2
{
    public static void Run()
    {
        int a = 2;
        int b = 4;
        Console.WriteLine($"somme : {a + b} produit : {a * b} quotient : {a / b}");
    }
}

class Exercice3
{
    public static void Run()
    {
        Console.WriteLine("Entrez une valeur décimale");
        string? usr_input = Console.ReadLine();
        double val = double.Parse(usr_input);
        Console.WriteLine($"la valeur arrondie est {Math.Round(val, 2)}");
    }
}

class Exercice4
{
    public static void Run()
    {
        int day_amount = 123;
        Console.WriteLine($"{day_amount} jours font {day_amount * 24} heures soit {day_amount * 24 * 60} minutes ou {day_amount * 24 * 60 * 60} secondes");
    }
}

class Exercice5
{
    public static void Run()
    {
        Console.WriteLine("Entrez un nombre à doubler");
        Console.WriteLine(int.TryParse(Console.ReadLine(), out int nbrToDouble) ? nbrToDouble * 2 : "Entrée invalide");
    }
}

class Exercice6
{
    public static void Run()
    {
        Console.WriteLine("Entrez un nombre décimal");
        Console.WriteLine(float.TryParse(Console.ReadLine(), out float decimalNbr) ? Convert.ToInt32(decimalNbr) : "Entrée invalide");
    }
}

class Exercice7
{
    public static void Run()
    {
        int celTemp = 20;
        Console.WriteLine($"{celTemp}°C fait {celTemp * (float)9 / (float)5 + 32}° en Fahrenheit");
    }
}
class Exercice8
{
    public static void Run()
    {
        if (!int.TryParse(Console.ReadLine(), out int Nbr))
        { Console.WriteLine("Entrée invalide"); }
        else
        {
            Console.WriteLine(Nbr % 2 == 0 ? "Le nombre est pair" : "Le nombre est impair");

        }
    }
}

class Exercice9
{
    public static void Run()
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
}
class Exercice10
{
    public static void Run()
    {
        var BBAN = "539007547034";
        var firstTen = double.Parse(BBAN[0..10]);
        var lastTwo = int.Parse(BBAN[10..]);
        Console.WriteLine((firstTen % 97 == lastTwo) || (firstTen % 97 == 0 && lastTwo == 97) ? "valide" : "invalide");
    }
}