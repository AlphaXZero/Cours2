using Bibliotheque;
namespace Utilisateurs
{
    class Etudiant(string nom, string prenom, List<Livre> livres)
    {
        public string Nom = nom;
        public string Prenom = prenom;
        public List<Livre> Livres = livres;
        public void AfficherInfo()
        {
            Console.WriteLine($"{Nom} {Prenom} possède ces livres :");
            foreach (Livre livret in Livres)
            {
                livret.AfficherInfo();
            }
        }
    }
}
