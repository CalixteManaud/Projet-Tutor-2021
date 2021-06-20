import numpy
import random
from tkinter import *
import time
import graphic
from graphic import *


def endgen(grid): #fonction vérifiant la fin de la génération du labyrinthe
    for j in range(1, len(grid), 2):
        for i in range(1, len(grid[j]), 2): #pour toutes les cases de la grilles qui ne sont pas des murs
            if grid[i][j] != grid[1][1]: #si la case actuelle n'est pas égale à la valeur de la première case alors la génération n'est pas finie
                return False
    return True


def grid_creator(grid, maze_size): #fonction créant la grille du labyrinthe
    k = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])): #pour chaque case
            if i % 2 == 0: #si la case se situe sur une colonne pair, définir sa valeur en -1 (mur)
                grid[i][j] = -1
            if j % 2 == 0: #si la case se situe sur une ligne pair, définir sa valeur en -1 (mur)
                grid[i][j] = -1
            if j == maze_size - 1: #si la case se sur les bords de la matrice, définir sa valeur en -1 (mur)
                grid[i][j] = -1
            if i == maze_size - 1: #si la case se sur les bords de la matrice, définir sa valeur en -1 (mur)
                grid[i][j] = -1
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[i][j] == 0: #pour chaque case, si ce n'est pas un mur, lui attribuer une valeur k différente à chaque fois
                k += 1
                grid[i][j] = k
    grid[1][0] = 1 #définir la valeur de l'entrée du labyrinthe à 1
    grid[maze_size - 2][maze_size - 1] = k #définir la valeur de la sortie du labyrinthe à k, le dernier nombre


def generate_maze(grid, maze_size, complexe): #fonction permettant la génération du labyrinthe
    finished = False
    grid_creator(grid, maze_size) #créer la grille
    while not endgen(grid): #tant que la génération n'est pas fini
        x = random.randint(1, maze_size - 2) #choisir un x aléatoire
        if x % 2 == 0: #si ce x se situe sur une colonne de mur
            y = random.randint(1, maze_size - 2) #chosir un y aléatoire
            if y % 2 == 0: #si ce y se situe sur une ligne de mur
                x -= 1 #décaler x de 1 pour être sur une colone de mur
                cell1 = grid[y - 1][x] #stocker la case en dessous
                cell2 = grid[y + 1][x] #stocker la case au dessus
            else: #si ce y ne se situe pas sur une ligne de mur
                cell1 = grid[y][x - 1] #stocker la case à gauche
                cell2 = grid[y][x + 1] #stocker la case à droite
        else: #sinon le x ne se situe pas sur une colonne de mur
            y = random.randint(1, maze_size - 2) #choisir un y aléatoire
            if y % 2 == 0: #si ce y se situe sur une ligne de mur
                cell1 = grid[y - 1][x] #stocker la case en dessous
                cell2 = grid[y + 1][x] #stocker la case au dessus
            else: #sinon ce y ne se situe pas sur une ligne de mur
                if x == 1: #si x se situe une colonne avant le bord
                    x += 1 #on décale x de 1
                    cell1 = grid[y][x - 1] #stocker la case à gauche
                    cell2 = grid[y][x + 1] #stocker la case à droite
                else:
                    x -= 1 #on décale x de -1
                    cell1 = grid[y][x - 1] #stocker la case à gauche
                    cell2 = grid[y][x + 1] #stocker la case à droite
        if cell1 != cell2: #si les deux cases stocker n'ont pas la même valeur
            grid[x][y] = 0 #changer la valeur de la case actuelle qui est un mur entre deux cases à 0
            for j in range(1, len(grid), 2):
                for i in range(1, len(grid[j]), 2):
                    if grid[j][i] == cell2: #chercher la case qui possède la valeur de cell2
                        grid[j][i] = cell1 #attribuer à la case la valeur stocker de cell1
    for j in range(1, len(grid)):
        if complexe: #si l'utilisateur demande un labyrinthe complexe
            x = random.randint(1, maze_size - 2)  #chosir x aléatoire
            if x % 2 == 0: #si ce x se situe sur une colonne de mur
                y = random.randint(1, maze_size - 2) #chosir un y aléatoire
                grid[y][x] = 0 #mettre la valeur de la case xy à 0 pour enlever des murs aléatoire dans le labyrinthe et le rendre complexe
    grid[1][0] = grid[1][1]
    grid[maze_size - 2][maze_size - 1] = grid[1][1]
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])): #parcourir la matrice
            if grid[i][j] > 0: #si la case n'est pas un mur lui attribuer pour valeur 0
                grid[i][j] = 0
    return grid


def distance(grid, maze_size): #fonction permettant de attribuer aux cases une distance à l'arrivée
    grid[maze_size - 2][maze_size - 1] = 1 #case à côté de l'arriver à pour distance 1
    k = 1
    while grid[1][1] == 0: #tant qu'on arrive pas à l'entrée du labyrinthe et qu'on ne change pas la valeur de la case à côté de l'entrée
        for j in range(len(grid) - 2, 0, -1):
            for i in range(len(grid[j]) - 2, 0, -1): #parcourir la matrice depuis l'arrivée
                if grid[i][j] == 0: #si la case actuelle n'est pas un mur
                    if grid[i + 1][j] > 0 or grid[i - 1][j] > 0 or grid[i][j + 1] > 0 or grid[i][j - 1] > 0: #si la à droite/gauche/en dessous/au dessus n'est pas un mur
                        k += 1
                        grid[i][j] = k #attribuer la valeur k qui est la distance qui augmente à la case actuelle
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0: #si une case est encore plus loin que l'arrivée de l'entrée
                grid[i][j] = k + 1 #lui attribuer la distance de l'arrivée à l'entrée + 1
    return grid


def solveMaze(grid, maze_size):
    x = 1
    y = 1
    graphic.changecell(0, 1)
    graphic.changecell(y, x)
    while x != maze_size - 1 and y != maze_size - 1: #tant que le programme n'est pas arrivé à la sortie du labyrinthe
        if grid[x][y] >= grid[x + 1][y] > 0: #si la case actuelle est supérieur à la case de droite, se déplacer vers cette case et la mettre à 0
            grid[x][y] = 0
            x += 1
            graphic.changecell(y, x)
        elif grid[x][y] >= grid[x - 1][y] > 0: #si la case actuelle est supérieur à la case de gauche, se déplacer vers cette case et la mettre à 0
            grid[x][y] = 0
            x -= 1
            graphic.changecell(y, x)
        elif grid[x][y] >= grid[x][y - 1] > 0: #si la case actuelle est supérieur à la case en-dessous, se déplacer vers cette case et la mettre à 0
            grid[x][y] = 0
            y -= 1
            graphic.changecell(y, x)
        elif grid[x][y] >= grid[x][y + 1] > 0: #si la case actuelle est supérieur à la case au-dessus, se déplacer vers cette case et la mettre à 0
            grid[x][y] = 0
            y += 1
            graphic.changecell(y, x)
    grid[1][0] = 0  #mettre la case de l'entrée du labyrinthe à 0
    grid[maze_size - 2][maze_size - 1] = 0 #mettre la case de la sortie du labyrinthe à 0


if __name__ == '__main__':
    g = graphic()
    g.end()
