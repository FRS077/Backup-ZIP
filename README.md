Description du Travail

Le script Python développé permet à l'utilisateur de créer une sauvegarde compressée d'un répertoire de son choix au format ZIP. Le fichier ZIP résultant est nommé selon le format opt_JJ-MM-AAAA.zip, où JJ-MM-AAAA représente la date de la sauvegarde.
Fonctionnalités Principales :

    Demande à l'utilisateur de spécifier le chemin du répertoire à compresser.
    Demande à l'utilisateur de spécifier le chemin de destination pour enregistrer le fichier ZIP.
    Crée un fichier ZIP contenant tous les fichiers et sous-répertoires du répertoire sélectionné.
    Vérifie que le répertoire source existe avant de tenter la compression.
    Affiche un message confirmant la fin du processus et le chemin du fichier ZIP créé.

Dépendances Nécessaires

Le script utilise les modules Python suivants :

    os : pour interagir avec le système de fichiers.
    zipfile : pour gérer la compression de fichiers au format ZIP.
    datetime : pour obtenir la date actuelle.

Ces modules sont inclus dans la bibliothèque standard de Python, donc aucune installation supplémentaire n'est nécessaire pour les utiliser.
Instructions pour l'Utilisation et le Lancement
Étape 1 : Installation de Python

Assurez-vous que Python 3 est installé sur votre système Debian. Vous pouvez vérifier la version de Python en exécutant la commande suivante dans un terminal :

python3 --version

Si Python n'est pas installé, vous pouvez l'installer avec la commande suivante :

sudo apt update  
sudo apt install python3
Pour exécuter le script, utilisez la commande suivante dans le terminal :

python3 backup.py

Suivez les instructions à l’écran pour entrer le chemin du répertoire que vous souhaitez compresser et le chemin où vous souhaitez enregistrer le fichier compressé.
Conclusion

Ce script simple et efficace permet de réaliser des sauvegardes de répertoires tout en offrant une flexibilité grâce à l'interaction avec l'utilisateur. Pour toute question ou besoin d'assistance supplémentaire, n'hésitez pas à demander !
