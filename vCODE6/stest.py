taches = []

def afficher_tache():
    if not taches:
        print("\nAucune taches en vue")
    else:
        print("\n===MES TACHES===")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")
            
            
def ajouter_tache():
    nouvelle_tache = input("\nVotre tache : ")
    taches.append(nouvelle_tache)
    print(f"Votre tache \'{nouvelle_tache}\' ajoutée avec succèes")
    
def supprimer_tache():
    if not taches:
        print("Vous n'avez aucune tache à supprimer")
        return
    
    afficher_tache()
    
    try:
        numero = int(input("L'Indice de la tache dont vous voulez supprimer : "))
        
        if 1 <= numero <= len(taches):
            tache_sup = taches.pop(numero - 1)
            print(f"Tache '{tache_sup} supprimée avec succèe")
        else:
            print("Indexe not correspondant à une tache, merci")
    except ValueError:
        print("Veuillez saisir un entier")
        
def modifier_tache():
    if not taches:
        print("Vous n'avez aucune tache à supprimer")
        return
    
    afficher_tache()
    
    try:
        numero = int(input("L'Indice de la tache dont vous voulez supprimer : "))
        
        if 1 <= numero <= len(taches):
            ancienne = taches[ numero - 1 ]
            nouvelle = input(f"Votre tache ? (Actuelle : '{ancienne}' : )")
            taches[numero - 1] = nouvelle
            print(f"Tache {ancienne} modifier en {nouvelle}")
        else:
            print("Indexe not correspondant à une tache, merci")
    except ValueError:
        print("Veuillez saisir un entier")
        
def sauvergarder_txt():
    with open("taches.txt", "w", encoding="utf-8") as f:
        for tache in taches:
            f.write(tache + "\n")
            
    print("Taches sauveegardées avec succèes")
    
def charger_txt():
    try:
        with open("taches.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                tache = ligne.strip()
                if tache:
                    taches.append(tache)
                    
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")
            
    except FileNotFoundError:
        print("→ Aucun fichier de sauvegarde trouvé. Nouveau départ !")
    
while True:
    print("\n---MENU---")
    print("1. Afficher taches")
    print("2. Ajouter tache")
    print("3. Supprimer tache")
    print("4. Modifier une tache")
    print("5. Sauvergarder les taches")
    print("6. Charger les taches sauvegarder")
    print("7. Quitter")
    
    choix = int(input("\nQuel est votre choix : "))
    
    if choix == 1:
        afficher_tache()
    elif choix == 2:
        ajouter_tache()
    elif choix == 3:
        supprimer_tache()
    elif choix == 4:
        modifier_tache()
    elif choix == 5:
        sauvergarder_txt()
    elif choix == 6:
        charger_txt()
    elif choix == 7:
        print("Au revoir")
        break
    else:
        print("Choix invalide, réessayer")
        
