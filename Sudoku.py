import random
from math import*
#test de commit
#autre de commit


def premiere_grille():
    lignes_un_deux_trois=[[1+(3*i+j)%9 for j in range(9)] for i in range(3)]
    lignes_quatre_cinq_six=[[lignes_un_deux_trois[i-3][(j+1)%3+3*(j//3)] for j in range(9)] for i in range(3,6)]
    lignes_sept_huit_neuf=[[lignes_quatre_cinq_six[i-3][(j+1)%3+3*(j//3)] for j in range(9)] for i in range(3,6)]
    return lignes_un_deux_trois+lignes_quatre_cinq_six+lignes_sept_huit_neuf

def affiche_grille(grille):
    for ligne in grille:
        print(ligne)

# region à l'intersection de la bande k et de la pile l
def extraire_region(k, l, grille):
    return [[grille[3*k+i][3*l+j] for j in range(3)] for i in range(3)]

def chiffre_aleatoire():
    return 1+int(9*random.random())


def region_du_nombre(i, j, grille):
    return extraire_region(i // 3, j // 3, grille)

def region_du_nombre_en_liste(i,j,grille):
    l=[]
    region=region_du_nombre(i, j, grille)
    for u in range(3):
        for v in range(3):
            l.append(grille[u][v])
    return l


#teste si on peut placer un chiffre en (i,j) en respectant les règles du jeu
def chiffre_possible(i, j, nouveau_chiffre, grille):
    for v in range(9):
        if grille[i][v]==nouveau_chiffre:
            return False
    for u in range(9):
        if grille[u][j]==nouveau_chiffre:
            return False
    bloc = region_du_nombre(i, j, grille)
    for u in range(3):
        for v in range(3):
            if bloc[u][v]==nouveau_chiffre:
                return False
    return True

def valeurs_possibles(i,j,grille):
    liste_valeurs_possibles=[]
    for nouveau_chiffre in range(1,10):
        if chiffre_possible(i, j, nouveau_chiffre, grille)==True:
            liste_valeurs_possibles.append(nouveau_chiffre)
    return liste_valeurs_possibles


def position_vers_coordonnees(position):
    return (position//9,position%9)

def coordonnees_vers_position(i,j):
    return 9*i+j


def coordonnees_du_suivant(i,j):
    return (i+(j+1)//9,(j+1)%9)



def grille_nulle():
    return [[0 for j in range(9)] for i in range(9)]



def resolution_grille_recursif(i,j,grille):
    if i==8 and j==8:
        return grille
    else:
        if grille[i][j]!=0:
            (u,v)=coordonnees_du_suivant(i,j)
            return resolution_grille_recursif(u,v,grille)
        else:
            for valeur in valeurs_possibles(i,j,grille):
                grille[i][j]=valeur
                (u, v) = coordonnees_du_suivant(i, j)
                if (resolution_grille_recursif(u,v,grille)!=grille_nulle()):
                    return resolution_grille_recursif(u,v,grille)
            else:
                grille[i][j]=0
                return grille_nulle()



def resolution_grille_sudoku(grille):
    i=0
    j=0
    while not (i==8 and j==8):
        if grille[i][j]!=0:
            (i,j)=coordonnees_du_suivant(i,j)
        else:
            liste_valeurs_possibles=valeurs_possibles(i,j,grille)
            if(len(liste_valeurs_possibles)==0):
                return grille
            else:
                index=0
                possibilitessuivant=False
                while((index<len(liste_valeurs_possibles)) and possibilitessuivant==False):
                    grille[i][j]=liste_valeurs_possibles[index]
                    (u,v)=coordonnees_du_suivant(i,j)
                    liste_valeurs_possibles_suivant=valeurs_possibles(u,v,grille)
                    if len(liste_valeurs_possibles_suivant)>0:
                        (i,j)=(u,v)
                        if ((i,j)==(8,8)):
                            grille[i][j]=liste_valeurs_possibles_suivant[0]
                        possibilitessuivant=True
                    else:
                        index+=1
                if possibilitessuivant==False:
                    return grille
    return grille


def valider_choix(i,j,grille):
    if i==8 and j==8:
        if grille[i][j]!=0:
            return True
        else:
            if len(valeurs_possibles(i, j, grille))>0:
                grille[i][j] = valeurs_possibles(i, j, grille)[0]
                return True
            else:
                return False
    else:
        if grille[i][j]!=0:
            (u,v)=coordonnees_du_suivant(i,j)
            return valider_choix(u,v,grille)
        else:
            for valeur in valeurs_possibles(i,j,grille):
                grille[i][j]=valeur
                (u, v) = coordonnees_du_suivant(i, j)
                if valider_choix(u,v, grille) == True:
                    return True
            else:
                grille[i][j]=0
                return False


def resoudre_grille(grille):
    valider_choix(0,0,grille)
    return grille



#seules les trois premières lignes sont aléatoires (fonction à revoir)
def grille_aleatoire():
    grille=[[0 for j in range(9)] for i in range(9)]
    for i in range(3):
        for j in  range(9):
            chiffre=chiffre_aleatoire()
            compteur=0
            while chiffre_possible(i,j,chiffre,grille)==False and compteur<100: #pour éviter la boucle sans fin!
                chiffre=chiffre_aleatoire()
                compteur=compteur+1
            if compteur<100:
                grille[i][j]=chiffre
            else:
                return [[0 for j in range(9)] for i in range(9)]
    for i in range(3,6):
        for j in range(9):
            grille[i][j]=grille[i-3][(j+1)%3+3*(j//3)]
    for i in range(6,9):
        for j in range(9):
            grille[i][j]=grille[i-3][(j+1)%3+3*(j//3)]
    return grille

#inutile pour l'instant
def permutation_de_s9():
    permutation=[chiffre+1 for chiffre in range(9)]
    random.shuffle(permutation)
    return permutation

#inutile également
def permutation_chiffres_grille(grille):
    permutation=permutation_de_s9()
    for i in range(9):
        for j in range(9):
            chiffre=grille[i][j]
            grille[i][j]=permutation[chiffre-1]
    return grille

def transposee(grille):
    return [[grille[j][i] for j in range(9)] for i in range(9)]

def echange_lignes(i,u,grille):
    grille[i],grille[u]=grille[u],grille[i]
    return grille

def echange_bandes(grille):
    k=int(3*random.random())
    m=int(3*random.random())
    while(k==m):
        k = int(3 * random.random())
        m = int(3 * random.random())
    for i in range(3):
        echange_lignes(3*k+i,3*m+i,grille)
    return grille

#echange deux lignes de la même bande
def echange_lignes_acceptable(grille):
    i=chiffre_aleatoire()-1
    u=chiffre_aleatoire()-1
    while (i//3!=u//3 or i==u):
        i = chiffre_aleatoire() - 1
        u = chiffre_aleatoire() - 1
    return echange_lignes(i,u,grille)

def echange_piles(grille):
    l=int(3*random.random())
    n=int(3*random.random())
    while(l==n):
        l = int(3 * random.random())
        n = int(3 * random.random())
    for j in range(3):
        echange_colonnes(3*l+j,3*n+j,grille)
    return grille


def echange_colonnes(j,v,grille):
    for i in range(9):
        grille[i][j],grille[i][v]=grille[i][v],grille[i][j]
    return grille

#échange deux colonnes de la même pile
def echange_colonnes_acceptable(grille):
    i=chiffre_aleatoire()-1
    u=chiffre_aleatoire()-1
    while (i//3!=u//3 or i==u):
        i = chiffre_aleatoire() - 1
        u = chiffre_aleatoire() - 1
    return echange_colonnes(i,u,grille)

#inutile pour l'instant
def echange_regions(k, l, m, n, grille):
    for i in range(3):
        for j in range(3):
            grille[3*k+i][3*l+j],grille[3*m+i][3*n+j]=grille[3*m+i][3*n+j],grille[3*k+i][3*l+j]
    return grille

#en fait non, cet échange crée de fausses grilles.
def echange_regions_acceptable(grille):
    k=int(3*random.random())
    l=int(3*random.random())
    m=int(3*random.random())
    n=int(3*random.random())
    while ((k==m and l==n) or (k!=m and l!=n)):
        k = int(3 * random.random())
        l = int(3 * random.random())
        m = int(3 * random.random())
        n = int(3 * random.random())
    return echange_regions(k, l, m, n, grille)

#les 3 premières lignes sont aléatoires puis on effectue diverses transformations
def grille_sudoku_aleatoire():
    grille_vide = [[0 for j in range(9)] for i in range(9)]
    grille=grille_vide
    while(grille[0][0]==0):
        grille=grille_aleatoire()
    for loop in range(15): #nombre un peu choisi au hasard...
        echange_lignes_acceptable(grille)
        echange_colonnes_acceptable(grille)
        transposee(grille)
        echange_bandes(grille)
        echange_piles(grille)
    return grille

#creation d'une grille à résoudre
def grille_a_resoudre(nombre_de_zeros):
    grille=grille_sudoku_aleatoire()
    nombre=0
    while nombre<nombre_de_zeros:
        i=chiffre_aleatoire()-1
        j=chiffre_aleatoire()-1
        if grille[i][j]!=0:
            grille[i][j]=0
            nombre=nombre+1
    return grille















