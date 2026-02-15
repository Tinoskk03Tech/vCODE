import tkinter as tk

print("Tkinter version:", tk.TkVersion)

fenetre = tk.Tk()


fenetre.title("Ma première app")

fenetre.geometry("1280x720")

fenetre.configure(bg="lightblue")

fenetre.resizable(False, False)


text = tk.Label(fenetre, text="Bienvenue dans mon application !", font=("Arial", 16), bg="lightblue")

text.pack(pady=50)

def text_modif () :
    text.config(text="Merci d'avoir cliqué !", foreground='blue')
    fenetre.configure(bg="green")


buttton = tk.Button(
    fenetre, 
    text="Cliquez ici", 
    command=text_modif
)


buttton.pack(padx=20, pady=20)

fenetre.mainloop()