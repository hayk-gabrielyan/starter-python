L = int(input("Veuillez saisir le nombre de lignes : "))
H = int(input("Veuillez saisir le nombre de colonnes : "))

# 1ère ligne
for i in range (1, 2): # hauteur de 1ère ligne
    for j in range (1, 2): # largeur de 1ère colonne de la 1ère ligne
        print("|" ,end="") # symbole de 1ère colonne de la 1ère ligne
    for k in range (1, L-1): # LARGEUR de la 1ère ligne
        print("-", end="") # symbole de milieu de la 1ère ligne
    print('|') # symbole de la fin de le 1ère ligne

# lignes milieu
for i in range (1, H-1): # HAUTEUR de tout
    for j in range (1, 2): # largeur de 1ère colonne du milieu
        print("|" ,end="") # symbole de 1ère colonne du milieu
    for k in range (1, L-1): # LARGEUR du vide du milieu
        print(" ", end="") # symbole de vide du milieu
    print('|') # symbole de la fin des lignes du milieu

# dernière ligne
for i in range (1, 2): # hauteur de dernière ligne
    for j in range (1, 2): # largeur de 1ère colonne de la dernière ligne
        print("|" ,end="") # symbole de 1ère colonne de la dernière ligne
    for k in range (1, L-1): # LARGEUR de la dernière ligne
        print("-", end="") # symbole de milieu de la dernière ligne
    print('|') # symbole de la fin de le dernière ligne
