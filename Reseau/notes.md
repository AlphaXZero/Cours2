## Types de réseaux
- PAN (personal) ex : bluetooth
- LAN (local) relie ordinateur et serveurs, ex : réseau entreprise
- MAN (metropolitan) connexion de réseaux entre eux, utilisé par fournisseurs pour relier concentrateurs
- WAN (wide) réseau étendu
- GAN internet

## Modèle OSI
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

## Modèle TCP/IP 
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

## La couche Physique
but = support pour transport des données binaires. Câbles ou ondes.

### PAM-5
- C'est le codage pour les câbles. + 5V ou - 5V.
- Combiné avec Modulation par Treillis.
- 5 ème lvl = redondance.

### RJ45 (8p8c)
- Quatres paires de fils en full-duplex (2 sens). Max 1 GB/s.
- Câble droit pr co ordi à switch/routeur.
- Câble croisé pr co 2 ordis ensemble. Obsolète.
- S'épuise après 5km.

### Firbre optique 
- Multimode = toutes les couleurs. LAN car 2KM.
- Monomode = 1 seul longueur d'onde. WAN car moins d'atténuation et 100km.

### Réseaux sans fils
- mélange de couche 1 et 2.

## Topologies

### Topologie en bus 
- 1 dorsale avec tous les autres co dessus


## Routage

En réalité, le masque ne sert qu'au routage. Si ordis sur même réseau, ils peuvent dialoguer via la couhce LNK.     
Si réseaux différents, système envoie les données en couche NET. le routeur dispose de plusieurs interfaces réseau. le routeur dispose de plusieurs adresses MAC.   
Le routeur possède une table de routage.

### IPV6 :
- espace d'adressage quasi infini.
- Simplifie le routage.
- On peut condigurer automatiquement des adresses.
- Unicast (point à point), Multicast (sous-groupe), anycast (celui qui a besoin va chercher info)

Elle est composée de 8 x 4 chiffres hexa séparés par ':'.
Souvent quand :0000:0000: => :::

### Protocole ARP

Rôle = correspondre adress IP et adress MAC.    
Envoie un message partout et attend un retour.  
"Je suis xx je dois joindre xx est-il sur réseau local ??"  
"Je suis Macadress xx et ip xx et je réponds à xxx"

### Protocole ICMP

permet au routeur de gérer infos relatives aux erreurs des machines connectées sur le réseau.

# Transport

Pour la couche 4, cette adress spécifique se nomme le port. Utlisé par les couches du dessus pour écouter les clients.  
les 1024 premiers ports sont réservés.

- Port 80 = porte éntrée internet (port HTTP).    
- Port 143 = port imap. (entrée des emails).  
- Port 20 et 21 = port FTP.   
- Port 443 = ports https.
- Port 25 = port smtp (envoie mail)
- Port 53 = DNS

Ordi peut être client et seveur. => netstat -an.    

Avant de se co au serv google. L'os va spécifier aléatoirment un port de connexion après les 1024. google utilisera ce port pour envoyer les réponses.  
Le serveur enverra en réponse un autre port choisi aléatoirment.

## TCP VS UDP

Transport control protocol = plus lent mais vérifie que bien arrivé  .   
Udp envoie juste.

Tcp = le plus utilisé. Permet transport fiable.     
Il reste en contact avec le correspondant.      
Contrôle chaque octet, Tcp va établir une co avec un système nommé THREE-WAY-HANDSHAKE

## QUICK
Mélange d'udp et tcp dévellopé par google.      
C'est le protocole de base au HTTP 3.0.

## Firewall
Le firewall va masquer les ports d'un ordinateur.       
Firewall matériel est inclus dans la box, ça masque tous les ports sauf le port 81 par exemple.     
Firewall software va mettre des gardiens sur ces ports ouverts.

# Application

Gérée par OS. DNS, DHCP et sockets.