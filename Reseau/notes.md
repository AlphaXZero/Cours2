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
