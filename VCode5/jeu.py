import tkinter as tk

print("Tkinter version:", tk.TkVersion)

fenetre = tk.Tk()


fenetre.title("Ma première app")

fenetre.geometry("720x580")

fenetre.configure(bg="beige")

fenetre.resizable(False, False)


text = tk.Label(fenetre, text="Bienvenue dans mon application !", font=("Arial", 16), bg="lightblue")

def affichage() :
    texte = textbox.get()
    text_saisi.config(text=f"Vous avez saisi : {texte}")

tk.Label(
    fenetre,
    text="Saisissez votre nom : "
).pack(pady=20)

textbox = tk.Entry(fenetre, font=("Comic Sans MS", 20), width=20)
textbox.pack(pady=20)

tk.Button(
    fenetre,
    text="Valider",
    command=affichage
).pack(pady=20)


text_saisi = tk.Label(fenetre, text="", font=("Comic Sans MS", 16), bg="beige")
text_saisi.pack(pady=20)

fenetre.mainloop()