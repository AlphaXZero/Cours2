#set text(font: "Roboto", fill: white)
#set page(fill: rgb("#111111"))
#set heading(numbering: "1.")


#show heading.where(
  level: 1,
): it => text(
  font: "Chilanka",
  size: 20pt,
  weight: "regular",
  style: "normal",
  it.body + linebreak(),
)

#show heading.where(
  level: 2,
): it => text(
  font: "Chilanka",
  size: 16pt,
  weight: "regular",
  style: "normal",
  it.numbering + " " + it.body + linebreak(),
)

= Projet d'analyse et conception d'applications

Choisir :
- netbeans 6.1 (\<6.8)
- eclipse 3.4 (mieux que netbeans)
- *visual paragdim community*
- ArgotUml
- uml designer

#linebreak()
== Use case diagram (diagramme de cas d'utilisations)

Voit excel\
les fonctions doivent être écrient du pdv de l'acteur (avec des cercles) \
use case = cas d'utilisations, ex: acteur utilise une fct° \
max 8/9 cas d'utilisations\
acteur doit obligatoirement interagir avec au moins 1 fonction\
acteurs à gauches : primaires\
acteurs à droites : secondaires : acteurs solicités par le système ex:  bankeys\
Par exemple, pour traiter le passage en caisse : le caissier est un acteur principale client est un acteur secondaire
Il peut y avoir des acteurs spécialisés qui héritent d'un autre acteur et qui ont un lien en plus\
Egalement entre les fonctions,
- "include" pour retirer de l'argent oblier de passer par s'authentifier\
- "extend" pour ajouter une fonction optionnelle ex: afficher solde(mettre une condition avec la flèche)\
metttre les priotités ensuite avec des itérations\
#linebreak()
#figure(
  image("./usecase.png", width: 80%),
)

== User story
décire les fonctions, quelles sont les étapes d'abord de manière triviale puis détaillé\
mettre la post condition\
Ex: retirer de l'argent = résultat attendu
postcondition : le client part avec sa thune
précondtion : le client est authentifié
Ex:
Traiter le passage en caisse
précondtion :  le tpv est en service, un caissier est connecté


=== Types de scénarios
- nominal : tout se passe bien
- alternatif : le client décide de ne pas acheter un article
- d'exception : le tpv ne répond pas
on detail tout après
titre
résumé
acteurs principal et secondaire
acteur à gauche et interraction avec le systeme à droite
voir slides profs

==
#linebreak()
