#set text(font: "Liberation Serif", 12pt)
#let bluee(body) = text(body, blue)
#set page(margin: 2cm, numbering: "-1-")
#set heading(numbering: "1.a")

#show raw.where(block: true): set block(
  stroke: (left: 3pt + luma(180), rest: none),
  inset: (left: 8pt, top: 6pt, bottom: 6pt),
  radius: 3pt,
  fill: luma(255),
)


WIP page de garde
#pagebreak()
#outline(title: "Table des matières")
#pagebreak()

= Préparation de la machine virtuelle
Nous avons choisis d'utilier VirtualBox ainsi que Ubuntu Server pour l'iso car c'est un des os les plus utilisés et la documentation est abondante. #bluee[@tuto]\
Pour l'installation, nous avons mis 4gb de RAM ainsi que 2 CPU et 50gb de stockage.\
Nous pouvons ensuite démarer la machine, et faire toute la configuration normalement en choisant la langue, la disposition du clavier, etc.\
Il faut néanmoins faire attention à ce que LVM group #bluee[@lvm] soit désactivé car c'est un gestionnaire de volumes logiques qui n'est pas compatible avec les configurations RAID qu'on utilisera plus tard.

#figure(
  rect(image("images/lvm.png", width: 100%), stroke: black, radius: 0.2cm),
  caption: [Configuration OS],
)<lvm>

une fois l'installation terminée, nous pouvons mettre à jour les paquets disponibles puis éteindre la machine pour poursuivre la configuration.
```
sudo apt update && sudo apt upgrade -y
sudo shutdown now
```
Nous avez également installer micro pour remplacer nano car c'est plus agréable à utiliser mais ce n'est pas obligatoire.
```
sudo apt install micro
```

= Configuration du réseau
== Configuration du réseau sur VirtualBox
Une fois la machine créé, nous éditons la configuration de la machine. #bluee[@config1]


#figure(
  rect(image("images/config1.png", width: 65%), stroke: black, radius: 0.2cm),
  caption: [Onglet configuration VirtualBox],
)<config1>

Dans l'onglet Réseau, nous passons le mode d'accès réseau en NAT (pas réseaux NAT) afin d'éviter que notre machine prenne une adresse ip déjà utilisé sur le réseau. #bluee[@confignat]

#figure(
  rect(image("images/config_nat.png", width: 80%), stroke: black, radius: 0.2cm),
  caption: [Onglet configuration Réseau],
)<confignat>

Cependant, nous n'avions plus d'accès Réseau après avoir configurer l'ip fixe plus loin. Pour être sûr on a donc créé un réseau Host-only #bluee[@confir1] #bluee[@configr2]  pour ensuite pourvoir créer notre 2ème adaptateur en réseau privé hôte. #bluee[@configr3]

#figure(
  rect(image("images/outils.png", width: 65%), stroke: black, radius: 0.2cm),
  caption: [Outils Network Manager],
)<confir1>

#figure(
  rect(image("images/réseau.png", width: 65%), stroke: black, radius: 0.2cm),
  caption: [Outils Network Manager],
)<configr2>

#figure(
  rect(image("images/adapt2.png", width: 65%), stroke: black, radius: 0.2cm),
  caption: [Onglet configuration Réseau - adapter 2],
)<configr3>

== Mise en place de l'ip fixe

Une fois ceci fini, nous pouvons lancer la machine et pour que notre server ai une ip fixe nous devons changer le netplan.
```
sudo micro /etc/netplan/50-netcfg.yaml
```
note : il faut bien changer le 50-netcfg.yaml et non le 1-netcfg.yaml car ça nous avait conduit à des problèmes.\
Puis, il faut y mettre ceci en respectant la syntaxe:
```
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: no
      addresses:
        - 192.168.56.10/24
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```
Dans addresses: on peut mettre l'ip qu'on veut du moment qu'elle est dans la range précédemment défini. #bluee[@configr2]\
Normalement enp0s3 et enp0s8 sont le nom des interfaces de base mais on peut vérifier avec ça avant:
```
ip a
```
#figure(
  rect(image("images/ipa.png", width: 100%), stroke: black, radius: 0.2cm),
  caption: [Résultat de la commande ip a],
)<ipaa>

Pour terminer, il faudra activer le netplan
```
sudo netplan apply
```

On peut aussi tester si l'accès à internet et au DNS est toujours bonne en pingant une addresse pour voir si les packets sont reçus:
```
ping google.com
```

= Stockage
Afin de protéger l'intégrité des données que les utilisateurs mettront sur le serveur, nous avons choisis une configuration de stockage RAID10. #bluee[@raidim]

#figure(
  rect(image("images/raid.png", width: 100%), stroke: black, radius: 0.2cm),
  caption: [Schéma d'un RAID10 #bluee[@raid]],
)<raidim>
Cette configuration #bluee[@raidcalcim] permet d'avoir une lecture plus rapide ainsi que la possibilité qu'au moins un disque tombe en panne sans altérer les fichiers, dans certains cas si les disques sont dans des unités différentes, on peut même aller jusqu'à 2 disques défaillants sans problèmes. Nous perdons cependant la moitié de notre capacité de stockage.
#figure(
  rect(image("images/raid_calc.png", width: 80%), stroke: black, radius: 0.2cm),
  caption: [Calcul des spécificités d'un RAID10 #bluee[@raid_calc]],
)<raidcalcim>
== Création des disques sur VirtualBox
Premièrement, nous avons créé les disques sur VirtualBox. Ils sont en VDI et on activer l'option "branchable à chaud" #bluee[@stockim]
#figure(
  rect(image("images/stock.png", width: 80%), stroke: black, radius: 0.2cm),
  caption: [Onglet Confiuration>Stockage de VirtualBox],
)<stockim>

== Partition des disques en mode RAID
Deuxièmement, nous avons partionné chaque disque en fd comme suit:
```
sudo fdisk /dev/sdb
n
enter (normalement le default est primary)
enter (normalement le default est 1)
enter
enter
```
maintenant on change le type de partition en fd
```
t
fd
```
et là on écrit et on quitte
```
w
```
il faut mainteant répéter l'opération pour chaque disk
```
sudo fdisk /dev/sdc
sudo fdisk /dev/sdd
sudo fdisk /dev/sde
```
on peut ensuite vérifier que tous les disks ont bien été partionné avec:
```
lsblk
```
== Création du RAID
On va installer mdadm pour créer le raid
```
sudo apt install mdadm -y
sudo mdadm --create /dev/md10 --level=10 --raid-devices=4 /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1
```
On peut vérifier que tout à bien marché avec:
```
sudo mdadm --detail /dev/md10
```
qui devrai sortir quelque chose comme ça. #bluee[@madd]
#figure(
  rect(image("images/madmd.png", width: 80%), stroke: black, radius: 0.2cm),
  caption: [Onglet Confiuration>Stockage de VirtualBox],
)<madd>
== Montage du RAID
On va d'abord formater le RAID.
```
sudo mkfs.ext4 /dev/md10
```
Et puis on créé un dossier pour enregistrer tous nos fichiers et on le monte.
```
sudo mkdir /data
sudo mount /dev/md10 /data
```
On peut vérifier avec:
```
df -h
```
On a bien Ldev/md10 qui est monté sur /data. #bluee[@mountt]
#figure(
  rect(image("images/mount.png", width: 80%), stroke: black, radius: 0.2cm),
  caption: [Onglet Confiuration>Stockage de VirtualBox],
)<mountt>
== Montage du RAID automatique au démarage
Pour faire en sorte que ça se monte automatiquement au démarage, on récupère l'UUID de notre périphérique
```
sudo blkid /dev/md10
```
Et on ajoute: *UUID={le uuid qu'on a eu plus haut} /data ext4 defaults,nofail 0 2* au fichier /etc/fstab:\
(il ne faut pas supprimer ce qui est déjà présent, on l'a testé à nos dépends et ça na rien donné de bon (: )\
```
sudo micro /etc/fstab
```
Enfin on sauvergarde la configuration.
```
sudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf
sudo update-initramfs -u
```
Le RAID devrait désormais être fonctionnel, on peut redémarrer et vérifier que tout continue de fonctionner et que /dev/md10 est toujours mount avec /data. #bluee[@dff]
```
reboot
cat /proc/mdstat
df -h
```
#figure(
  rect(image("images/dfh.png", width: 80%), stroke: black, radius: 0.2cm),
  caption: [Onglet Confiuration>Stockage de VirtualBox],
)<dff>

= Adminsitration à distance avec openssh-server
== Installation
Pour que la connexion à distance soit sécurisé,nous allons utliser le protocole SSH #bluee[@ssh]:
```
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```
Il devrait maintenant être en active si on fait:
```
sudo systemctl status ssh
```
== Accéder au server avec ssh
Mainteant que openssh-server a été installé avec succès, nous pouvons nous connecter depuis notre pc avec l'adresse ip fixe précédemment définit ainsi que l'utilisateur. #bluee[@ipaa]
```
ssh alpa@192.168.56.11
```
= Adminsitration à distance avec interface web légère
== Installation
Pour réaliser l'objectif d'accéder au server depuis une interface web légère, nous avons choisis d'utiliser Webmin #bluee[@webmin].
```
curl -o webmin-setup-repo.sh https://raw.githubusercontent.com/webmin/webmin/master/webmin-setup-repo.sh
sudo sh webmin-setup-repo.sh
sudo apt install --install-recommends webmin
```
== Accéder à la page
On peut ainsi se connecter depuis notre navigateur sur notre vm client grâce à cette url:\
* https://192.168.56.11:10000 * (l'ip est à remplacé par celle qu'on avait définit)

#pagebreak()

#bibliography("refs.bib", title: "Références")

