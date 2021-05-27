import numpy
import random
from tkinter import *
from graphic import *

def endgen(grid):
    for j in range(1, len(grid), 2):
        for i in range(1, len(grid[j]), 2):
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
    """for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == -1:
                t.changecell(root, i, j, True)
            else:
                t.changecell(root, i, j, False)
            root.update()
    root.mainloop()"""


def generate_maze(grid, maze_size, complexe):
    finished = False
    grid_creator(grid, maze_size)
    while not endgen(grid):
        x = random.randint(1, maze_size - 2)
        if x % 2 == 0:
            y = random.randint(1, maze_size - 2)
            if y % 2 == 0:
                if x == 1:
                    x += 1
                    cell1 = grid[y - 1][x]
                    cell2 = grid[y + 1][x]
                else:
                    x -= 1
                    cell1 = grid[y - 1][x]
                    cell2 = grid[y + 1][x]
            else:
                cell1 = grid[y][x - 1]
                cell2 = grid[y][x + 1]
        else:
            y = random.randint(1, maze_size - 2)
            if y % 2 == 0:
                cell1 = grid[y - 1][x]
                cell2 = grid[y + 1][x]
            else:
                if x == 1:
                    x += 1
                    cell1 = grid[y][x - 1]
                    cell2 = grid[y][x + 1]
                else:
                    x -= 1
                    cell1 = grid[y][x - 1]
                    cell2 = grid[y][x + 1]
        if cell1 != cell2:
            grid[x][y] = 0
            for j in range(1, len(grid), 2):
                for i in range(1, len(grid[j]), 2):
                    if grid[j][i] == cell2:
                        grid[j][i] = cell1
    grid[1][0] = grid[1][1]
    grid[maze_size - 2][maze_size - 1] = grid[1][1]
    print(grid)


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
    pass