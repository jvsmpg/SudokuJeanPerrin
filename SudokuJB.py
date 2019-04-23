#fonction qui donne la liste des valeurs que l'in peut mettre ‡ la ligne et colonne de grille
#L est l'ensemble des choix possibles
L = [1,2,3,4,5,6,7,8,9]
#fonction qui affecte la valeur ‡ la position intiquÈe dans la grille passÈe en paramËtre
def affecte_valeur(position,valeur,grille):
    indice_ligne = int(position / 9)
    indice_colonne = position % 9
    grille[indice_ligne][indice_colonne] = valeur
#fonction qui donne la valeur du coefficient de grille ‡ la position passÈe en paramËtre
def valeur_position(position,grille):
    indice_ligne = int(position / 9)
    indice_colonne = position % 9
    return grille[indice_ligne][indice_colonne]
#fonction qui extrait la ligne de la grille a l'indice passÈ en paramËtre
def extraire_ligne(indice,grille):
    l = []
    for j in range(0, 9):
        l.append(grille[indice][j])
    return l
#fonction qui extrait la colonne de la grille ‡ l'indice passÈ en paramËtre
def extraire_colonne(indice,grille):
    l = []
    for i in range(0,9):
        l.append(grille[i][indice])
    return l
#fonction qui extrait le bloc corrspondant ‡ la ligne et ‡ la colonne passÈe en paramËtre
def extraire_bloc(ligne,colonne,grille):
    l = []
    if ligne in range(0,3):#si on est entre la ligne 1 et 3
        if colonne in range(0,3):#si on est entre la colonne 1 et 3
            for i in range (0,3):
                for j in range(0,3):
                    l.append(grille[i][j])
        else:
            if colonne in range(3, 6):#si on est entre la colonne 4 et 6
                for i in range(0, 3):
                    for j in range(3, 6):
                        l.append(grille[i][j])
            else:
                if colonne in range(6,9):#si on est entre la colonne 7 et 9
                    for i in range (0,3):
                        for j in range(6,9):
                            l.append(grille[i][j])
    if ligne in range(3, 6):#si on est entre la ligne 4 et 7
            if colonne in range(0, 3):#si on est entre la colonne 1 et 3
                for i in range(3, 6):
                    for j in range(0, 3):
                        l.append(grille[i][j])
            else:
                if colonne in range(3, 6):#si on est entre la colonne 4 et 6
                    for i in range(3, 6):
                        for j in range(3, 6):
                            l.append(grille[i][j])
                else:
                    if colonne in range(6, 9):#si on est entre la colonne 7 et 9
                        for i in range(3, 6):
                            for j in range(6, 9):
                                l.append(grille[i][j])
    else:
        if ligne in range(6, 9):  # si on est entre la ligne 7 et 9
            if colonne in range(0, 3):
                for i in range(6, 9):
                    for j in range(0, 3):
                        l.append(grille[i][j])
            else:
                if colonne in range(3, 6):
                    for i in range(6, 9):
                        for j in range(3, 6):
                            l.append(grille[i][j])
                else:
                    if colonne in range(6, 9):
                        for i in range(6, 9):
                            for j in range(6, 9):
                                l.append(grille[i][j])
    return l


#fonction qui donne la liste des choix possible ‡ la position passÈe en paramËtre
def choix_possible(position,grille):
    #recuperer la position dans la grille
    indice_ligne = int(position/9)
    indice_colonne = position%9
    l = set(extraire_ligne(indice_ligne, grille))
    c = set(extraire_colonne(indice_colonne, grille))
    b = set(extraire_bloc(indice_ligne, indice_colonne, grille))
    liste = set(L).difference(l.union(c.union(b)))
    liste = list(liste)  # reconvertir l'ensemble en liste indexÈe
    return liste

# fonction rÈcursive qui precise si on peut remplir en position suivante ‡ partir du choix fait en position courante
def valider_choix(position_courante,grille):
    if position_courante == 80:
        return True
    else:
        if valeur_position(position_courante,grille)!= 0:
            return valider_choix(position_courante+1,grille)
        else:
            for choix in choix_possible(position_courante,grille):
                affecte_valeur(position_courante, choix, grille)
                if valider_choix(position_courante + 1, grille) == True:
                    return True
            else:
                affecte_valeur(position_courante, 0, grille)
                return False




grille = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

#fonction qui complete la grille passÈe en paramËtre
def genere_grille(grille):
    valider_choix(0,grille)
    return grille

genere_grille(grille)
print(grille)