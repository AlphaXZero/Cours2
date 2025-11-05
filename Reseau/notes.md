# Types de réseaux
- PAN (personal) ex : bluetooth
- LAN (local) relie ordinateur et serveurs, ex : réseau entreprise
- MAN (metropolitan) connexion de réseaux entre eux, utilisé par fournisseurs pour relier concentrateurs
- WAN (wide) réseau étendu
- GAN internet

# Modèle OSI
Modèle théorique, norme qui explique comment ordinateur communique entre eux.
- 7. Application (on intéragit avec ordi)
- 6. Présentation (ordi va faire une requête http)
- 5. Session (crétion de la session avec serveur)
- 4. Trasnport
- 3. Résau
- 2. Liaison
- 1. Physique

Pas utilisé en pratique car
- on utilisait déjà le tcp/ip
- trop complet/complexe, tcp/ip + opti et efficace
- c'était lent comparé au tcp/ip

# Modèle TCP/IP 
il n'y a que 4 couches

 OSI | TCP/IP 
-----|--------
Application | HTTPS, DNS DHCP FTP 
Présentation | HTTPS, DNS DHCP FTP  
Session | HTTPS, DNS DHCP FTP  
Transport | TCP, UDP
Réseau | IPv4, IPv6
Liaison de données| PPP, Frame Relay, Ethernet
Physique|PPP, Frame Relay, Ethernet

- la couche liason et physique sont combinées grâce au protocole ethernet
- la couche réseau devient internet, c'est ce qui réalise la jonction entre les différents réseaux, elle injecte les trames IP(pauqets) dans un réseau et les achemine jusqu'a destination, c'est donc le protocle IP
-la couche transport est la même, transporte les données d'un endroit à un autre. avec TCP/UDP.

# Modèle hybride
- Application
- Transport (segment)
- Réseau (paquet)
- Liaison de données (trames) 
- Physique

## La couche Physique
but = support pour transport des données binaires. Câbles ou ondes.

### PAM-5
- C'est le codage pour les câbles. + 5V ou - 5V.
- Combiné avec Modulation par Treillis.
- 5 ème lvl = redondance et modulation par Treillis.

#### RJ45 (8p8c)
- Quatres paires de fils en full-duplex (2 sens). Max 1 GB/s.
- Câble droit pr co ordi à switch/routeur.
- Câble croisé pr co 2 ordis ensemble. Obsolète.
- S'épuise après 5km.

#### Firbre optique 
- Multimode = toutes les couleurs. LAN car 2KM.
- Monomode = 1 seul longueur d'onde. WAN car moins d'atténuation et 100km.

#### Réseaux sans fils
- mélange de couche 1 et 2.

### Topologies
- Topologie en bus   
 -> 1 dorsale avec tous les autres co dessus
- Topologie en étoile   
 -> tous les ordis sont réliés à un concentrateur, si un câble tombe c'est ok car un seul pc tombe.
- Topologie en anneau   
 -> semblable à bus mais la dorsale est co à elle-même, un seul noeud ne peut communiquer à la fois, en pratique il y a un token qui parcourir l'anneau et seul le noeud qui a le token peut communqiuer sur l'anneau. Mtn géré par un MAU (répartiteur).
- Maillage  
 -> évolution de l'étoile, plusieurs liasons point par point, chaque noeud est connecté à chaque autre noeud. Onéreux car chauqe noeud doit avoir autant de carte réseau et câble que de noeud.
- Arbre 
 -> dérive de l'étoile, faire des branches, moins couteux que maillage.

### Le hub
Ou répétiteur, pièce d'équipement de la topolgie en étoile. Couche 1, gère les données bruts, amplifie le signal reçu et transfère à tous les autres.   
Pb car envoie à tout le monde, qd bcp de co -> collisions de paquets.   
-> obsolète, mtn switch qui gère couche 2 aussi.

### CSMA/CD et CA
- Pour éviter collision, CSMA/CD (collision detection).     
 -> chaque terminal écoute en perma     
 -> terminal peut parler qui si personne parle     
 -> si collision, les 2 machines doivent attendre un tps random     
 -> reparle

 - CSMA/CA (Collision avoidance)      
 -> envoie msg d'avertissement avant de parler, si collision avert alors CSMA/CD

## La couche liaison
Assure co entre machines sur un réseau local. Tranférer données entre différents terminaux et corriger certaines erreurs de la couche physique.

### Réseau ethernet et adresse mac
#### MAC
Addresse mac = identifiant unique pour machine.
Composée de 48 bits, 6 octets écrits en hexa séparé par :.
Décomposé comme suit :
- 1bit I/G pour indiquer si adresse individuelle ou groupe d'addresse (switch)
- 1bit U/L pour adresse universelle ou administrée localement
- 22 bits pour identifier l'entreprise qui a fait l'équipement réseau.
- 24 bits d'adresse unique. identifiant de la carte réseau.

L'addresse FF:FF:FF:FF:FF:FF est l'adresse de broadcast qui permet d'adresser toutes les machines d'un réseau local.

#### La trame ethernet
Protcole le plus employé dans la couche 2.
- Min 64 octets et max 1518.
6oct destination MAC | 6oct source MAC | 2oct EtherType | 46 - 1500 oct Payload | 4oct crc

#### switch
S'occupe de la couche 2. Boîtier avec plusieurs 8p8, contrairement au hub qui envoie partout, le switch décode l'entête de la trame pour l'envoyer au bon port, donc meilleur que hub qui envoie les données sur tous les ports.    
Le switch possède une table de correspondace avec des mac adresses (port du switch à mac adress).   
- PC1 envoie à PC2  
si switch a macadd pc2 dans table -> envoie    
sinon envoie à tout le monde    
switch meilleur que hub car collissions moindres. CSMA/CD moins solicité. switch = full-duplex

## La couche réseau
### Protocole IP
- ip = numéro identification logique.     
- 2 ordis communiquent ensembles grâce à carte réseau en envoyant des trames contenant l'adresse de destination.
#### classes d'addresses
avant classes (a grande ,b moy ,c pt)   
mtn,CIDR, pour diminuer taille table de routage     

fournisseur donne un bloc d'addresses afin de créer des sous réseaux

#### adress ipV4
32 bits regoupés en 4 octets.
max 2^32
notation séparé par .
#### addresse ipv6
128 bits soit 16 octets.
notation en hexa séparé par :   
adresses sont réservés :
- 0.0.0.0 ou ::0    
route par défaut
- 127.0.0.1 (ou ::1)    
localhost
- adresse de diffusion ou brodcast  
désigne tous les postes du réseua   
mettre tous les bits réservé à 1 pour l'obtenir
- adresses privés
#### masques de sous réseau
distinguer bits adresse ip utilisés pour identifier sous réseau de ceux de hôte. adresse de sous réseau obtenu en faisant un AND entre ip et masque     
ne sert qu'au routeur pour savoir sur quelle couche comuniquer
### protocole ARP
table arp conserve assocations MAC/IP.  
- pour que ordi connait mac du routeur :              
ordinateur va émettre requêtre arp (192.168.0.1 ou ::O) et routeur va envoyer son adress mac. les 2 écrivent dans leur table.

### protocole ICMP
utiliser par routeur, permet de vérifier les erreurs
## Routeur
relier réseaux entre eux et choisir meilleur chemin.        
- les routeurs sont dotés de connecteurs appelés port de gestion. 
pas utiliser pour transfert paquet 
- possèdent plusieurs interfaces réseaux chaque interface permet de se connecter à un réseau, le routeur possède plusieurs adresses MAC     
- possède table de routage avec liste des autres routeurs.
### Route
route par défaut => route à suivre si connait pas adresse destination, ça s'appelle passerelle.
#### Exemple
adr mac routeur | adr mac source | type |

## Couche Transport

Pour la couche 4, cette adress spécifique se nomme le port. Utlisé par les couches du dessus pour écouter les clients.  
les 1024 premiers ports sont réservés.

- Port 80 = porte éntrée internet (port HTTP).    
- Port 143 = port imap. (entrée des emails).  
- Port 20 et 21 = port FTP.   
- Port 443 = ports https.
- Port 25 = port smtp (envoie mail)
- Port 53 = DNS

### exemple 
navigateur interroge par défaut le port 80 d'un serveur, l'os va spécifier aléatoirement un port de connexion et faire une demande en specifiant son port, le serveur enverra l'autorisation / son port aussi ce qui libérera le port 80

### TCP (transport control protocol)
connecté, controle que chaque octet est bien reçu avec three way handshake avec des numéros de quéquences

### udp
simplifié, plus rapide, utilisé pour streaming par ex. pas besoin de savoir destination.
### firewall
- firewall matériel filtrer les ports et les masques
- firewall logiciel controle les accès des différentes applis web avec gardiens
## Couche Application
### dns
- domain name system
serveur DNS c'est ce qui traduit le nom en adresse ip.
- Quand on tape une adresse, ou envoie une requête dns query à un serveur dns en lui demandant l'adresse ip. Si dns connait il envoie une requête dns reponse avec l'adresse. sinon demande à un autre dns si personne connait envoie nulle
### dhcp
dynamic host configuration, gère les adresses ip des ordi co.       
dhcp donne une adresse ip temporaire valable un certains temps.
### http
hypertexte transfer protocol
permet de tranferer des fichiers html grace à url entre nav et serv.
### ssh
permet de faire une session protégé avec un serv.


