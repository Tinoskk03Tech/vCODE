# Calculatrice intelligente en Python
print("\n\n\t\t=== CALCULATRICE INTELLIGENTE ===")


while True:
    # Demander à l'utilisateur d'entrer deux nombres
    a = float(input("\nEntrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))

    # Afficher les options d'opération disponibles
    print("\nChoisissez l'opération à effectuer ( +, -, *, /, ** ) :")

    # Demander à l'utilisateur de choisir une opération
    operation = input("\tOpération : ")

    # Effectuer le calcul en fonction de l'opération choisie
    if operation == "+":
        # Afficher le résultat de l'addition
        print(f"\nRésultat : {a} + {b} = {a + b}")
        
    elif operation == "-":
        # Afficher le résultat de la soustraction
        print(f"\nRésultat : {a} - {b} = {a - b}")
        
    elif operation == "*":
        # Afficher le résultat de la multiplication
        print(f"\nRésultat : {a} * {b} = {a * b}")
        
    elif operation == "/":
        # Vérifier si le dénominateur n'est pas zéro avant de faire la division
        if b != 0:
            print(f"\nRésultat : {a} / {b} = {a / b}")
        else:
            print("\nErreur : Division par zéro n'est pas autorisée.")
            
    elif operation == "**":
        # Afficher le résultat de l'exponentiation
        print(f"\nRésultat : {a} ** {b} = {a ** b}")
        
    else:
        # Afficher un message d'erreur si l'opération choisie n'est pas valide
        print("\nOpération invalide. Veuillez choisir parmi +, -, *, /, **.")
        
    # Demander à l'utilisateur s'il souhaite effectuer un autre calcul
    continuer = input("\nVoulez-vous effectuer un autre calcul ? ( o / n ) : ")
    if continuer.lower() != "o":
        print("\nMerci d'avoir utilisé la calculatrice intelligente. \n\tAu revoir !\n")
        break