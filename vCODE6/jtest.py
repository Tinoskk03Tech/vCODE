import json
import os


taches = []

def afficher_menu():
    print("\n" + "=" * 40)
    print("     TODO LIST - GESTION DE TÂCHES")
    print("=" * 40)
    print("1. Afficher tous les taches")
    print("2. Ajouter une tache")
    print("3. Marquer comme terminée")
    print("4. Supprimer une tache")
    print("5. Modifier une tache")
    print("6. Sauvergarder")
    print("7. Quitter")

def afficher_taches():
    if not taches:
        print("\n✓ Aucune tâche pour le moment.")
        return
    
    print("\n" + "-" * 40)
    print("          LISTE DES TÂCHES")
    print("-" * 40)
    for i, tache in enumerate(taches, 1):        
        statut = "✓" if tache["terminee"] else "○"        
        titre = tache["titre"]        
        # Affichage avec statut
        if tache["terminee"]:            
            print(f"{statut} {i}. [{titre}] (Terminée)")        
        else:            
            print(f"{statut} {i}. {titre}")    
    print("-"*40)    
    print(f"Total : {len(taches)} tâche(s)")
            
            
def ajouter_tache():
    """Ajoute une nouvelle tâche"""
    titre = input("\nTitre de la tâche : ").strip()    
    if not titre:        
        print("⊠ Le titre ne peut pas être vide !")        
        return
        
    nouvelle_tache = {        
            "titre": titre,        
            "terminee": False    
                      }    
    taches.append(nouvelle_tache)    
    print(f"✓ Tâche '{titre}' ajoutée !")
    
def marquer_terminee():    
    """Marque une tâche comme terminée"""    
    if not taches:        
        print("\n⊠ Aucune tâche à marquer !")        
        return    
    
    afficher_taches()  
      
    try:        
        numero = int(input("\nNuméro de la tâche à marquer : "))        
        if 1 <= numero <= len(taches):            
            taches[numero - 1]["terminee"] = True            
            titre = taches[numero - 1]["titre"]            
            print(f"✓ Tâche '{titre}' marquée comme terminée !")        
        else:            
            print("⊠ Numéro invalide !")    
        
    except ValueError:        
        print("⊠ Entre un numéro valide !")
    
    
def supprimer_tache():
    if not taches:
        print("Vous n'avez aucune tache à supprimer")
        return
    
    afficher_taches()
    
    try:
        numero = int(input("L'Indice de la tache dont vous voulez supprimer : "))
        
        if 1 <= numero <= len(taches):
            tache_supprimee = taches.pop(numero - 1)
            print(f"✓ Tâche '{tache_supprimee['titre']}' supprimée !")
        else:
            print("⊠ Numéro invalide !")
    except ValueError:
        print("⊠ Entre un numéro valide !")
        
def modifier_tache():    
    """Modifie une tâche existante"""    
    if not taches:        
        print("\n⊠ Aucune tâche à modifier !")        
        return    
    
    afficher_taches() 
       
    try:        
        numero = int(input("\nNuméro de la tâche à modifier : "))        
        if 1 <= numero <= len(taches):            
            ancienne = taches[numero - 1]["titre"]            
            nouvelle = input(f"Nouveau titre ('{ancienne}') : ").strip()            
            if nouvelle:                
                taches[numero - 1]["titre"] = nouvelle
                print(f"✓ Tâche modifiée : '{ancienne}' → '{nouvelle}'")            
            else:                
                print("⊠ Le titre ne peut pas être vide !")        
        else:            
            print("⊠ Numéro invalide !")    
            
    except ValueError:
        print("⊠ Entre un numéro valide !")
        
        
        
def sauvegarder():    
    """Sauvegarde les tâches dans un fichier JSON"""    
    try:        
        with open("taches.json", "w", encoding="utf-8") as fichier:            
            json.dump(taches, fichier, indent=2, ensure_ascii=False)        
            print("✓ Tâches sauvegardées dans 'taches.json' !")    
    except Exception as e:        
        print(f"⊠ Erreur lors de la sauvegarde : {e}")
        

def charger():    
    """Charge les tâches depuis le fichier JSON"""    
    global taches
    
    if not os.path.exists("taches.json"):        
        print("→ Aucun fichier de sauvegarde. Nouveau départ !")        
        return    
    
    try:        
        with open("taches.json", "r", encoding="utf-8") as fichier:            
            taches = json.load(fichier)        
            print(f"✓ {len(taches)} tâche(s) chargée(s) !")    
        
    except Exception as e:        
        print(f"⊠ Erreur lors du chargement : {e}")
        


# === PROGRAMME PRINCIPAL ===
def main():    
    """Fonction principale"""    
    print("\n● BIENVENUE DANS TODO LIST ●")    
    print("-" * 40)    
    # Charger les tâches au démarrage    
    charger()    
    
    # Boucle principale    
    while True:        
        afficher_menu()        
        choix = input("\nTon choix : ").strip() 
               
        if choix == "1":            
            afficher_taches()        
            
        elif choix == "2":
            ajouter_tache()        
            
        elif choix == "3":            
            marquer_terminee()        
        
        elif choix == "4":            
            supprimer_tache()        
        
        elif choix == "5":            
            modifier_tache()        
        
        elif choix == "6":            
            sauvegarder()        
        
        elif choix == "7":            
            # Sauvegarder avant de quitter            
            sauvegarder()            
            print("\n● À bientôt ! ●\n")            
            break        
        
        else:            
            print("\n⊠ Choix invalide !")
      
      
      
# Point d'entrée
if __name__ == "__main__":
    main()