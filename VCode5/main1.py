import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première app")
fenetre.geometry("1280x720")
fenetre.config(bg="Blue")

compteur = 0
lb_cpt = tk.Label(
    fenetre, 
    text=f"Click : {compteur}", 
    font=("Comic Sans MS", 16, "bold"), 
    bg="Green",
    padx = 20,
    pady = 20
)

lb_cpt.pack()


def incrementer() :
    global compteur
    compteur += 1
    lb_cpt.config(
        text = f"Click : {compteur}"
    )


button = tk.Button(
    fenetre,
    text = "Click me !",
    font = ("Comic Sans MS", 20, "bold"),
    bg = "Yellow",
    fg = "Red",
    activebackground="Green",
    relief="flat",
    cursor="hand2",
    command = incrementer 
)

button.pack()

#bouton = tk.Button(fenetre, command=lambda: saluer("tkossi")

fenetre.mainloop()