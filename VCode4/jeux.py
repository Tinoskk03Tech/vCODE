import random

print("\n\t=========================================")
print("\t JEU DE DEVINETTE DE NOMBRE ")
print("\t=========================================")

# Accueil du joueur
print("\nBienvenue dans le jeu de devinette de nombre !")

# Générer un nombre secret entre 1 et 100
nombre_secret = random.randint(1, 100)

# Initialiser le nombre de tentatives
tentative = 1

# Initialiser la variable de contrôle
trouve = False

# Boucle principale du jeu
while True :
    # Demander à l'utilisateur de deviner le nombre
    while not trouve :
        # Gérer les erreurs de saisie
        try :
            nombre_utilisateur = int(input("\nDevinez le nombre secret entre 1 et 100 : "))
        except ValueError:
            print("\tVeuillez entrer un nombre valide.")
            continue

        # Vérifier la devinette de l'utilisateur
        if ( nombre_secret > nombre_utilisateur ) :
            print("\tPlus haut ")
        elif ( nombre_secret < nombre_utilisateur ) :
            print("\tPlus bas ")
        else :
            print("\tFélicitations ! Vous avez trouvé le nombre secret !")
            trouve = True
        # Incrémenter le nombre de tentatives
        tentative += 1

        # Afficher le nombre secret et le nombre de tentatives
        print("\nLe nombre secret était : ", nombre_secret)
        # Afficher le nombre de tentatives
        print("\tVous avez trouvé à la ", tentative, "ème tentative !")

        # Demander à l'utilisateur s'il veut rejouer
        rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").strip().lower()
        # Gérer les réponses de l'utilisateur
        if rejouer != 'oui' :
            print("\nMerci d'avoir joué ! Au revoir !")
            break
        else :
            # Réinitialiser le jeu
            nombre_secret = random.randint(1, 100)
            tentative = 1
            trouve = False
