# ---------------------------------------
# Script de sauvegarde et compression ZIP  
# Auteur : Romuald FRS077  
# Email : fra485@orange.fr  
# ---------------------------------------

import os  
import zipfile  
from datetime import datetime

def backup_with_zip(source_dir, output_dir):
    # Vérifier si le répertoire source existe  
    if not os.path.exists(source_dir):
        print(f"Le répertoire {source_dir} n'existe pas.")
        return

    # Créer un nom de fichier ZIP avec la date au format JJ-MM-AAAA  
    current_date = datetime.now().strftime('%d-%m-%Y')
    output_zip_file = os.path.join(output_dir, f'opt_{current_date}.zip')  # Chemin complet du fichier ZIP de sortie

    # Créer un fichier ZIP  
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Ajouter tous les fichiers et sous-répertoires  
        for dirpath, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                # Ajouter le fichier au ZIP avec le chemin relatif  
                zipf.write(file_path, os.path.relpath(file_path, source_dir))

    print(f"Sauvegarde et compression terminées : {output_zip_file}")

# Demander à l'utilisateur d'entrer le chemin du répertoire source et de la destination  
source_directory = input("Entrez le chemin du répertoire à compresser : ")  
output_directory = input("Entrez le chemin où vous voulez que le fichier compressé soit enregistré : ")  

backup_with_zip(source_directory, output_directory)
