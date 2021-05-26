import numpy
import random
from tkinter import *
from graphic import *

def endgen(grid):
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[i][j] != grid[1][1]:
                return False
    return True

def grid_creator(grid, maze_size):
    k = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if i % 2 == 0:
                grid[i][j] = -1
            if j % 2 == 0:
                grid[i][j] = -1
            if j == maze_size-1:
                grid[i][j] = -1
            if i == maze_size - 1:
                grid[i][j] = -1
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[i][j] == 0:
                k += 1
                grid[i][j] = k
    grid[1][0] = 1
    grid[maze_size - 2][maze_size - 1] = k
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == -1:
                t.changecell(root, i, j, True)
            else:
                t.changecell(root, i, j, False)
            root.update()
    root.mainloop()


def generate_maze(grid, maze_size, complexe):
    finished = False
    grid_creator(grid, maze_size)
    while endgen(grid):
        a = maze_size - 2
        b = maze_size - 1
        x = random.randint(0, a)
        x += 1
        if x % 2 == 0:
            #b = b/2
            y = random.randint(0, b)
            y = y + 1
        else:
            #a = a/2
            y = random.randint(0, a)
            y = y + 2
        if grid[x-1][y] == -1:
            cell1 = grid[x][y - 1]
            cell2 = grid[x][y + 1]
        else:
            cell1 = grid[x - 1][y]
            cell2 = grid[x + 1][y]
        if cell1 != cell2:
            grid[x][y]
            for j in range(0, len(grid)):
                for i in range(0, len(grid[j])):
                    if grid[i][j] == cell2:
                        grid[i][j] = cell1
    if complexe:
        for j in range(0, len(grid)):
            x = random.randint(0, a)
            x += 1
            if x % 2 == 0:
                #b = b/2
                y = random.randint(0, b)
                y = y + 1
            else:
                #a = a/2
                y = random.randint(0, a)
                y = y + 2
            grid[x][y] = 0
#    print(grid)
    #for j in range(0, len(grid)):
     #   for i in range(0, len(grid[j])):



if __name__ == '__main__':
    root = Tk()
    t = Table(root)
    sizeerror = True
    erreurC = True
    complexe = False
    while sizeerror:
        try:
            maze_size = int(input("Quelle taille de labyrinthe voulez vous ? Saisissez un taille impaire entre "
                                  "10 et 50 : "))
            if 10 <= maze_size <= 50 and maze_size % 2 == 1:
                sizeerror = False
                break
            print("La taille n'est pas valide !")
        except Exception:
            print("Veuillez mettre une bonne valeur !")
    while erreurC:
        try:
            c = str(input("Le labyrinthe est-il complexe ? (o/n) : "))
            if c == 'o':
                complexe = True
                break
            elif c == 'n':
                complexe = False
                break
            print("Saisissez 'o' ou 'n' !")
        except Exception:
            print("Veuillez mettre 'o' ou 'n' !")
    grid = numpy.array([[0] * maze_size] * maze_size)
    generate_maze(grid, maze_size, complexe)