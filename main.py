from tkinter import *
from tkinter import messagebox

def creation_joueurs(*args):
    tableau_nombre_joueurs.pop()
    for i in range(int(nombre_joueurs_entry.get())):
        tableau_nombre_joueurs.append(i+1)
    print(tableau_nombre_joueurs)
    fenetre_nombre_joueurs.destroy()

def fonction_nom_joueurs(*args):
    nouveau_joueur_label = Label(fenetre_nom_joueurs, text=f"Joueur {len(compteur)+1} : {nom_joueurs_entry.get()}")
    nouveau_joueur_label.pack(pady=5)
    tableau_nom_joueurs.append(nom_joueurs_entry.get())
    nom_joueurs_entry.delete(0, END)
    compteur.append(0)
    if len(compteur) == len(tableau_nombre_joueurs):
        nom_joueurs_entry.config(state="disabled")
        fenetre_nom_joueurs.after(1500, fenetre_nom_joueurs.destroy)
    print(tableau_nom_joueurs)

def ajout_score(*args):
    score_joueur = Label(tableau_score_score_total_joueur[0][len(nom_introuvable)], text=entry_score_joueur.get())
    score_joueur.pack(pady=1, side="left")
    tableau_score_joueur[len(nom_introuvable)].append(int(entry_score_joueur.get()))
    tableau_score_score_total_joueur[1][len(nom_introuvable)].config(text=sum(tableau_score_joueur[len(nom_introuvable)]))
    entry_score_joueur.delete(0, "end")
    nom_introuvable.append(0)
    try:
        messagebox.showinfo("",f"C'est à {tableau_nom_joueurs[len(nom_introuvable)]} de jouer !")
    except IndexError:
        nom_introuvable.clear()
        messagebox.showinfo("", f"C'est à {tableau_nom_joueurs[len(nom_introuvable)]} de jouer !")
    tableau_label_joueur[len(nom_introuvable)-1].config(fg="black")
    tableau_label_joueur[len(nom_introuvable)].config(fg="red")
    print(len(nom_introuvable))

tableau_nombre_joueurs = [0]
nombre_de_joueurs = int(tableau_nombre_joueurs[0])
compteur = []
tableau_nom_joueurs = []
nom_introuvable = []

fenetre_nombre_joueurs = Tk()
fenetre_nombre_joueurs.title("Nombre de joueurs")
fenetre_nombre_joueurs.resizable(width=False, height=False)

frame_nombre_joueurs = Frame(fenetre_nombre_joueurs)
frame_nombre_joueurs.pack(padx=30, pady=30)

nombre_joueurs_label = Label(frame_nombre_joueurs, text="Nombre de joueurs :\n(Appuyez sur entrée pour valider)", font=("Arial", 20))
nombre_joueurs_label.pack()

nombre_joueurs_entry = Entry(frame_nombre_joueurs)
nombre_joueurs_entry.bind("<Return>", creation_joueurs)
nombre_joueurs_entry.pack()

fenetre_nombre_joueurs.mainloop()

tableau_score_joueur = [
    [] for i in tableau_nombre_joueurs
]

print(tableau_score_joueur)

fenetre_nom_joueurs = Tk()
fenetre_nom_joueurs.title("Nom des joueurs")
fenetre_nom_joueurs.resizable(width=False, height=False)

frame_nom_joueurs = Frame(fenetre_nom_joueurs)
frame_nom_joueurs.pack(padx=30, pady=30)

nom_joueurs_label = Label(frame_nom_joueurs, text="Donnez le nom des joueurs :\n(Appuyez sur entrée pour valider)", font=("Arial", 15))
nom_joueurs_label.pack()

nom_joueurs_entry = Entry(frame_nom_joueurs)
nom_joueurs_entry.bind("<Return>", fonction_nom_joueurs)
nom_joueurs_entry.pack()

fenetre_nom_joueurs.mainloop()

boucle_principale = Tk()
boucle_principale.title("Boucle de jeu")
boucle_principale.resizable(width=False, height=False)

frame_principale = Frame(boucle_principale)
frame_principale.pack(padx=30, pady=30)

tableau_score_score_total_joueur = [
    [],
    []
]

tableau_label_joueur = []

for i in tableau_nom_joueurs:
    frame_i = Frame(frame_principale)
    frame_i.pack(fill="x")
    label_nom_joueur = Label(frame_i, text=i, font=("", 10))
    label_nom_joueur.pack(side="left")
    frame_score_i = Frame(frame_i)
    frame_score_i.pack(fill="x", padx=5, side="left")
    label_score_total_i = Label(frame_i, text=0, font=("bold", 10))
    label_score_total_i.pack(side="right")
    tableau_score_score_total_joueur[0].append(frame_score_i)
    tableau_score_score_total_joueur[1].append(label_score_total_i)
    tableau_label_joueur.append(label_nom_joueur)

bouton_arret_jeu = Button(boucle_principale, text="Terminer la partie et afficher les résultats...", fg="white", bg="red", command=boucle_principale.destroy)
bouton_arret_jeu.pack(padx=5, pady=5, side="bottom")

messagebox.showinfo("Début du jeu",f"C'est à {tableau_nom_joueurs[0]} de jouer !")
tableau_label_joueur[0].config(fg="red")

entry_score_joueur = Entry(boucle_principale)
entry_score_joueur.bind("<Return>", ajout_score)
entry_score_joueur.pack()

boucle_principale.mainloop()

score_totaux_joueurs = [sum(tableau_score_joueur[i]) for i in range(len(tableau_nom_joueurs))]

if len(tableau_nom_joueurs) == 1:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici votre score :\n{score_totaux_joueurs[0]}")
elif len(tableau_nom_joueurs) == 2:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici les résultats :\n{tableau_nom_joueurs[0]} : {sorted(score_totaux_joueurs)[-1]}\n{tableau_nom_joueurs[1]} : {sorted(score_totaux_joueurs)[-2]}")
elif len(tableau_nom_joueurs) == 3:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici les résultats :\n{tableau_nom_joueurs[0]} : {sorted(score_totaux_joueurs)[-1]}\n{tableau_nom_joueurs[1]} : {sorted(score_totaux_joueurs)[-2]}\n{tableau_nom_joueurs[2]} : {sorted(score_totaux_joueurs)[-3]}")
else:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici les résultats :\n{tableau_nom_joueurs[0]} : {sorted(score_totaux_joueurs)[-1]}\n{tableau_nom_joueurs[1]} : {sorted(score_totaux_joueurs)[-2]}\n{tableau_nom_joueurs[2]} : {sorted(score_totaux_joueurs)[-3]}\nEt les autres, on s'en fiche...")