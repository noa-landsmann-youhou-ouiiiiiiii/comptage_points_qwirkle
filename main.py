from tkinter import *
from tkinter import messagebox

def creation_joueurs(*args):
    try:
        if nombre_joueurs_entry.get() and not nombre_joueurs_entry.get().isspace():
            tableau_nombre_joueurs.pop()
            for i in range(int(nombre_joueurs_entry.get())):
                tableau_nombre_joueurs.append(i+1)
            print(tableau_nombre_joueurs)
            fenetre_nombre_joueurs.destroy()
    except ValueError:
        pass

def fonction_nom_joueurs(*args):
    if int(nombre_joueurs_entry.get()):
        nouveau_joueur_label = Label(fenetre_nom_joueurs, text=f"Joueur {len(compteur)+1} : {str(nom_joueurs_entry.get())}")
        nouveau_joueur_label.pack(pady=5)
        tableau_nom_joueurs.append(str(nom_joueurs_entry.get()))
        nom_joueurs_entry.delete(0, END)
        compteur.append(0)
        if len(compteur) == len(tableau_nombre_joueurs):
            nom_joueurs_entry.config(state="disabled")
            fenetre_nom_joueurs.after(1500, fenetre_nom_joueurs.destroy)
        print(tableau_nom_joueurs)
    else:
        nom_joueurs_entry.delete(0, "end")

def ajout_score(*args):
    try:
        if entry_score_joueur.get() and not entry_score_joueur.get().isspace():
            score_joueur = Label(tableau_score_score_total_joueur[0][len(joueur_a_qui_cest_le_tour_index)], text=int(entry_score_joueur.get()))
            score_joueur.pack(pady=1, side="left")
            tableau_score_joueur[len(joueur_a_qui_cest_le_tour_index)].append(int(entry_score_joueur.get()))
            tableau_score_score_total_joueur[1][len(joueur_a_qui_cest_le_tour_index)].config(text=sum(tableau_score_joueur[len(joueur_a_qui_cest_le_tour_index)]))
            joueur_a_qui_cest_le_tour_index.append(0)
            try:
                messagebox.showinfo("",f"C'est à {tableau_nom_joueurs[len(joueur_a_qui_cest_le_tour_index)]} de jouer !")
            except IndexError:
                joueur_a_qui_cest_le_tour_index.clear()
                messagebox.showinfo("", f"C'est à {tableau_nom_joueurs[len(joueur_a_qui_cest_le_tour_index)]} de jouer !")
            tableau_label_joueur[len(joueur_a_qui_cest_le_tour_index) - 1].config(fg="black")
            tableau_label_joueur[len(joueur_a_qui_cest_le_tour_index)].config(fg="red")
            print(len(joueur_a_qui_cest_le_tour_index))
    except ValueError:
        label_erreur.config(text="erreur")
    entry_score_joueur.delete(0, "end")

tableau_nombre_joueurs = [0]
nombre_de_joueurs = int(tableau_nombre_joueurs[0])
compteur = []
tableau_nom_joueurs = []
joueur_a_qui_cest_le_tour_index = []

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

label_erreur = Label(boucle_principale, text="abc", fg="red")
label_erreur.pack()

bouton_arret_jeu = Button(boucle_principale, text="Terminer la partie et afficher les résultats...", fg="white", bg="red", command=boucle_principale.destroy)
bouton_arret_jeu.pack(padx=5, pady=5, side="bottom")

messagebox.showinfo("Début du jeu",f"C'est à {tableau_nom_joueurs[0]} de jouer !")
tableau_label_joueur[0].config(fg="red")

entry_score_joueur = Entry(boucle_principale)
entry_score_joueur.bind("<Return>", ajout_score)
entry_score_joueur.pack()

boucle_principale.mainloop()

score_totaux_joueurs_fin = [sum(tableau_score_joueur[i]) for i in range(len(tableau_nom_joueurs))]
score_totaux_joueurs_fin[len(joueur_a_qui_cest_le_tour_index)] += 6

if len(tableau_nom_joueurs) == 1:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici votre score :\n{score_totaux_joueurs_fin[0]}")
elif len(tableau_nom_joueurs) == 2:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici les résultats :\n{tableau_nom_joueurs[0]} : {score_totaux_joueurs_fin[0]}, {tableau_nom_joueurs[1]} : {score_totaux_joueurs_fin[1]}")
elif len(tableau_nom_joueurs) == 3:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici les résultats :\n{tableau_nom_joueurs[0]} : {score_totaux_joueurs_fin[0]}, {tableau_nom_joueurs[1]} : {score_totaux_joueurs_fin[1]}, {tableau_nom_joueurs[2]} : {score_totaux_joueurs_fin[2]}")
else:
    messagebox.showinfo("Fin de la partie",f"Félicitaions ! Voici les résultats :\n{tableau_nom_joueurs[0]} : {score_totaux_joueurs_fin[0]}, {tableau_nom_joueurs[1]} : {score_totaux_joueurs_fin[1]}, {tableau_nom_joueurs[2]} : {score_totaux_joueurs_fin[2]},\nEt les autres, on s'en fiche...")