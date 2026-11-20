#fichier avec la logique mathématique du puissance 4

def creer_grille() -> list :
    return [[0 for _ in range(7)] for _ in range (6)]

def colonne_pleinne(grille, colonne):
    pass

def poser_jeton(grille, colonne, joueur):
    pass

def a_gagne(grille, joueur):
    pass

def grille_pleine(grille):
    pass



# test
grille = creer_grille()

def afficher_grille(grille):
    for ligne in grille:
        print(ligne)

