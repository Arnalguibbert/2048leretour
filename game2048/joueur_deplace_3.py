

def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    if not Verify(move):
        move= input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

def read_size_grid():
    size = int(input("Entrez la taille de la grille:"))
    return size

def read_theme_grid():
    theme = str(input("Entrez le numero de theme choisi:"))
    return theme



