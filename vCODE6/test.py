taches = []

# print(type(taches))

taches.append("Apprendre Python")

# print(taches)

with open("taches.txt", "w") as fichier:
    for tache in taches:
        fichier.write(tache + "\n")
        
with open("taches.txt", "r") as fichier:
    contenu = fichier.read()
    
print(contenu)