import subprocess
import os

def run_script(script_path):
    """Exécute un script Python et gère les erreurs."""
    try:
        print(f"Exécution de {script_path}...")
        subprocess.run(["python", script_path], check=True)
        print(f"{script_path} terminé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {script_path}: {e}")
    except FileNotFoundError:
        print(f"Erreur : python n'est pas trouvé. Assurez-vous qu'il est installé et dans votre PATH.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")

if __name__ == "__main__":
    # Chemins vers vos scripts (ajustez si nécessaire)
    scripts = [
        "C:\\Users\\hp\\Downloads\\STAGIAIRE SCRAPING\\stage_1.py",
        "C:\\Users\\hp\\Downloads\\STAGIAIRE SCRAPING\\unique.py",
        "C:\\Users\\hp\\Downloads\\STAGIAIRE SCRAPING\\stage_2.py",
        "C:\\Users\\hp\\Downloads\\STAGIAIRE SCRAPING\\fusion.py",
        "C:\\Users\\hp\\Downloads\\STAGIAIRE SCRAPING\\filter.py",
    ]

    # Exécution des scripts dans l'ordre
    for i, script in enumerate(scripts):
        if os.path.exists(script):
            run_script(script)
            if i < len(scripts) - 1:  # Vérifie si ce n'est pas le dernier script
                print(f"\nLancement du prochain script : {scripts[i+1]}\n")
        else:
            print(f"Erreur : {script} n'existe pas dans le chemin spécifié.")

    # Mise à jour automatique dans Git
    try:
        os.chdir("C:\\Users\\hp\\Downloads\\STAGIAIRE SCRAPING") #navigue vers le bon dossier
        os.system("git add offres_avec_lien.json offres_sans_lien.json")
        os.system("git commit -m 'Mise à jour automatique des fichiers JSON'")
        os.system("git push origin main")
        print("Mise à jour Git réussie.")
    except Exception as git_error:
        print(f"Erreur lors de la mise à jour Git : {git_error}")