



# Configuration initiale
def initialiser_grille():
    return [' ' for _ in range(9)]

grille = initialiser_grille()


# Fonction pour afficher la grille
def afficher_grille(grille):
    print(f"{grille[0]} | {grille[1]} | {grille[2]}")
    print("--+---+--")
    print(f"{grille[3]} | {grille[4]} | {grille[5]}")
    print("--+---+--")
    print(f"{grille[6]} | {grille[7]} | {grille[8]}")

afficher_grille(grille)


# Fonction pour prendre l'entrée d'un joueur
def prendre_entree_joueur(joueur, grille):
    while True:
        try:
            position = int(input(f"Joueur {joueur}, entrez une position (1-9) : ")) - 1
            if position < 0 or position > 8:
                print("Position invalide. Veuillez entrer un nombre entre 1 et 9.")
            elif grille[position] != ' ':
                print("Cette case est déjà prise. Veuillez en choisir une autre.")
            else:
                grille[position] = joueur
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Exemple d'utilisation
prendre_entree_joueur('X', grille)
afficher_grille(grille)

# Fonction pour vérifier les conditions de victoire
def verifier_victoire(grille, joueur):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for combinaison in combinaisons_gagnantes:
        if all(grille[i] == joueur for i in combinaison):
            return True
    return False

# Exemple d'utilisation
print(verifier_victoire(grille, 'X'))


def jouer_tic_tac_toe():
    grille = initialiser_grille()
    joueur_actuel = 'X'
    tours = 0

    while tours < 9:
        afficher_grille(grille)
        prendre_entree_joueur(joueur_actuel, grille)

        if verifier_victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Félicitations ! Joueur {joueur_actuel} a gagné !")
            return

        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
        tours += 1

    afficher_grille(grille)
    print("C'est un match nul !")


# Commencer le jeu
jouer_tic_tac_toe()
