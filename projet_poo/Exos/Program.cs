using System;

class Program
{
    static void Main(string[] args)
    {
        // Exercice1.Run();
        // Exercice2.Run();
        // Exercice3.Run();
        // Exercice4.Run();
        Exercice5.Run();
        // Exercice6.Run();
        // Exercice7.Run();
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
