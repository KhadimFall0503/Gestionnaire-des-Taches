import tkinter as tk
from tkinter import messagebox

def ajouter_tache():
    tache = entry_tache.get()
    if tache:
        taches.append({'tache': tache, 'marquee': False})
        lister_taches()
        entry_tache.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche.")

def supprimer_tache():
    try:
        index = int(listbox_taches.curselection()[0])
        tache_supprimee = taches[index]['tache']
        if messagebox.askyesno("Confirmation", f"Supprimer la tâche '{tache_supprimee}' ?"):
            del taches[index]
            lister_taches()
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à supprimer.")

def marquer_tache():
    try:
        index = int(listbox_taches.curselection()[0])
        taches[index]['marquee'] = not taches[index]['marquee']  # toggle
        lister_taches()
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à marquer/démarquer.")

def vider_taches():
    if messagebox.askyesno("Confirmation", "Vider toutes les tâches ?"):
        taches.clear()
        lister_taches()

def lister_taches():
    listbox_taches.delete(0, tk.END)
    for tache in taches:
        marque = "✅" if tache['marquee'] else "🔲"
        listbox_taches.insert(tk.END, f"{marque} {tache['tache']}")

def enregistrer_taches():
    with open("tache.txt", "w") as fichier:
        for tache in taches:
            ligne = f"{tache['tache']}|{tache['marquee']}\n"
            fichier.write(ligne)
    messagebox.showinfo("Succès", "Tâches enregistrées.")

def charger_taches():
    try:
        with open("tache.txt", "r") as fichier:
            for ligne in fichier:
                parts = ligne.strip().split('|')
                if len(parts) == 2:
                    titre, marquee_str = parts
                    taches.append({'tache': titre, 'marquee': marquee_str == 'True'})
                else:
                    # Gestion des anciennes lignes sans '|'
                    taches.append({'tache': parts[0], 'marquee': False})
        lister_taches()
    except FileNotFoundError:
        pass  # Aucun fichier, pas grave


# Initialiser
taches = []
root = tk.Tk()
root.title("Gestionnaire de tâches")
root.geometry("700x400")
root.resizable(width=False, height=False)
root.config(bg="#333333")

# Widgets
label_tache = tk.Label(root, text="Tâche:", bg="#333333", fg="white", font=("Arial", 12))
entry_tache = tk.Entry(root, width=50, font=("Arial", 12))
button_ajouter = tk.Button(root, text="Ajouter", command=ajouter_tache, bg="#4CAF50", fg="white")
button_supprimer = tk.Button(root, text="Supprimer", command=supprimer_tache, bg="#F44336", fg="white")
button_marquer = tk.Button(root, text="Marquer", command=marquer_tache, bg="#2196F3", fg="white")
button_enregistrer = tk.Button(root, text="Enregistrer", command=enregistrer_taches, bg="#FF9800", fg="white")
button_vider = tk.Button(root, text="Vider", command=vider_taches, bg="#9E9E9E", fg="white")
listbox_taches = tk.Listbox(root, width=60, height=10, font=("Arial", 12))

# Placement
label_tache.grid(row=0, column=0, padx=5, pady=5)
entry_tache.grid(row=0, column=1, padx=5, pady=5)
button_ajouter.grid(row=0, column=2, padx=5, pady=5)
button_supprimer.grid(row=1, column=0, padx=5, pady=5)
button_marquer.grid(row=1, column=1, padx=5, pady=5)
button_enregistrer.grid(row=1, column=2, padx=5, pady=5)
button_vider.grid(row=3, column=2, padx=5, pady=5)
listbox_taches.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

# Charger les tâches existantes
charger_taches()

# Lancer
root.mainloop()
