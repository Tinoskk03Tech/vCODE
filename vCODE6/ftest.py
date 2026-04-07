
# taches = ["Learn Python", "Learn Git&Github"]
taches = []

def sauvergarder_txt():
    with open("taches.txt", "w", encoding="utf-8") as f:
        for tache in taches:
            f.write(tache + "\n")
            
    print("Taches sauveegardées avec succèes")
    

# sauvergarder_txt()

def charger_txt():
    try:
        with open("taches.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                tache = ligne.strip()
                if tache:
                    taches.append(tache)
    except FileNotFoundError:
        print("→ Aucun fichier de sauvegarde trouvé. Nouveau départ !")
        
        
charger_txt()

for i, tache in enumerate(taches, 1):
    print(f"{i}. {tache}")

