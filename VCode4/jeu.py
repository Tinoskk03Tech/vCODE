import random
import time

print("\n\t=========================================")
print("\t        JEU DE DEVINETTE DE NOMBRE       ")
print("\t=========================================")

# Accueil du joueur
print("\nBienvenue dans le jeu de devinette de nombre amélioré !")

while True:
    # --- CHOIX DU NIVEAU ---
    print("\nChoisissez un niveau de difficulté :")
    print("1. Facile    (1 à 50   - 60 secondes)")
    print("2. Normal    (1 à 100  - 45 secondes)")
    print("3. Difficile (1 à 200  - 30 secondes)")

    while True:
        choix_niveau = input("Votre choix (1, 2 ou 3) : ")

        # Configuration selon le choix
        if choix_niveau == '1':
            max_nombre = 50
            temps_limite = 60
            break
        elif choix_niveau == "2":
            max_nombre = 100
            temps_limite = 45
            break
        elif choix_niveau == '3':
            max_nombre = 200
            temps_limite = 30
            break
        else:
            # Par défaut niveau Normal
            print(f'Veuillez saisir un nombre compris entre 1 et 3')

    # Générer le nombre secret
    nombre_secret = random.randint(1, max_nombre)

    # Initialisation
    tentative = 0
    trouve = False

    print(f"\nC'est parti ! Vous avez {temps_limite} secondes.")
    # Démarrage du chronomètre
    input('Entrez pour commencer')
    debut_temps = time.time()

    # Boucle de devinette
    while not trouve:
        # Calcul du temps restant
        temps_ecoule = time.time() - debut_temps
        temps_restant = temps_limite - int(temps_ecoule)

        # Vérifier si le temps est écoulé AVANT de demander
        if temps_restant <= 0:
            print("\n\t⏰ DRING ! Le temps est écoulé !")
            print(f"\tVous avez perdu. Le nombre secret était : {nombre_secret}")
            break

        print(f"\nTemps restant : {temps_restant}s")

        try:
            # On demande le nombre
            saisie = input(f"Devinez le nombre entre 1 et {max_nombre} : ")
            nombre_utilisateur = int(saisie)
        except ValueError:
            print("\t⚠️ Veuillez entrer un nombre valide.")
            continue

        # Vérifier si le temps est écoulé PENDANT la saisie (si le joueur a été lent à taper)
        if (time.time() - debut_temps) > temps_limite:
            print("\n\t⏰ Trop tard ! Vous avez mis trop de temps à répondre.")
            print(f"\tLe nombre secret était : {nombre_secret}")
            break

        # Incrémenter le nombre de tentatives (seulement après une saisie valide)
        tentative += 1

        # Vérifier la devinette
        if nombre_secret > nombre_utilisateur:
            print("\t⬆️  C'est plus HAUT !")
        elif nombre_secret < nombre_utilisateur:
            print("\t⬇️  C'est plus BAS !")
        else:
            temps_final = int(time.time() - debut_temps)
            print("\n\t🎉 Félicitations ! Vous avez trouvé le nombre secret !")
            print(f"\tLe nombre secret était bien : {nombre_secret}")
            print(f"\tVous avez réussi en {tentative} tentative(s) et en {temps_final} secondes.")
            trouve = True

    # Demander à l'utilisateur s'il veut rejouer
    rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").strip().lower()
    if rejouer != 'oui':
        print("\nMerci d'avoir joué ! Au revoir !")
        break