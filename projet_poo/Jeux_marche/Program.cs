using System;
class Program
{
    static void Main(string[] args)
    {
        Marche.init();
    }
}

class Marche
{

    public static void init()
    {
        string[] cart = new string[5];
        while (true)
        {
            Console.WriteLine("-------------------\nMENU MON PANIER\n-------------------\n1-ajouter fruits\n2-retier fruits\n3-afficher fruits\n4-rechercher fruits\n5-quitter ce menu");
            int input;
            int.TryParse(Console.ReadLine(), out input);
            switch (input)
            {
                case 1:
                    Console.Write("quelle fruit voulez vous ajouter ? -> ");
                    string? fruit = Console.ReadLine();
                    cart = add_cart(cart, fruit);
                    break;
                case 2:
                    Console.Write("quelle fruit voulez vous retirer ? -> ");
                    string? fruit2 = Console.ReadLine();
                    cart = del_cart(cart, fruit2);
                    break;
                case 3:
                    show_cart(cart);
                    break;
                case 4:
                    Console.Write("quelle fruit voulez vous chercher ? -> ");
                    string? fruit3 = Console.ReadLine();
                    search_fruits(cart, fruit3);
                    break;
                case 5:
                    return;
                default:
                    Console.WriteLine("option non trouvée, réessayez");
                    break;

            }
        }
    }
    static void show_cart(string[] cart)
    {
        foreach (string item in cart)
        {
            Console.Write($"{item} ");
        }
        Console.WriteLine();
    }
    static string[] add_cart(string[] cart, string? fruit)
    {
        if (cart.Contains(fruit))
        {
            Console.WriteLine("cette article existe déjà dans le panier !");
            return cart;
        }
        for (int i = 0; i < cart.Length; i++)
        {
            if (cart[i] == null)
            {
                cart[i] = fruit;
                return cart;
            }
        }
        Console.WriteLine("Il n'y a plus de places dans le panier !");
        return cart;
    }
    static string[] del_cart(string[] cart, string? fruit)
    {
        if (!cart.Contains(fruit))
        {
            Console.WriteLine("cette article n'existe pas dans le panier !");
            return cart;
        }
        for (int i = 0; i < cart.Length; i++)
        {
            if (cart[i] == fruit)
            {
                cart[i] = null;
                break;
            }
        }
        return cart;
    }

    static void search_fruits(string[] cart, string? fruit)
    {
        Console.WriteLine(cart.Contains(fruit) ? "le fruit est dans le panier" : "le fruit n'est pas dans le panier");
    }
}