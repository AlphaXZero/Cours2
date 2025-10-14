namespace Bibliotheque
{
    class Livre(string titre, string auteur, int annee)
    {
        public string Titre = titre;
        public string Auteur = auteur;
        public int Annee = annee;
        public void AfficherInfo()
        {
            Console.WriteLine($"Le livre \"{Titre}\" a été écris en {Annee} par {Auteur}");
        }
    }
}