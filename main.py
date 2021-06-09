import numpy
import random
import tkinter as tk
from graphic import *
from tkinter import ttk


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
            if j == maze_size - 1:
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
    print(grid)
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
    for j in range(1, len(grid)):
        if complexe:
            x = random.randint(1, maze_size - 2)
            if x % 2 == 0:
                y = random.randint(1, maze_size - 2)
                grid[y][x] = 0
    grid[1][0] = grid[1][1]
    grid[maze_size - 2][maze_size - 1] = grid[1][1]
    createLab(grid)


def createLab():
    root = Tk()
    root.title("Labyrinthe")
    root.geometry("1900x1000")
    root.attributes('-fullscreen', True)
    root.lift()
    canvas = Canvas(root, height=5000, width=5000, scrollregion=(0, 0, 3000, 3000))
    hbar = Scrollbar(root, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=canvas.xview)
    vbar = Scrollbar(root, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    l = Label(root, text="Quelle taille de labyrinthe voulez vous ?\nSaisissez un taille impaire entre "
                         "10 et 50 : ", pady=5)
    l.config(font=("Courier", 10), pady=5)
    t = Text(root, height=2, width=10)
    varcb = False
    l.pack()
    t.pack
    c = Checkbutton(root, text="Le Labyrinthe est-il complexe ?", pady=5, variable=varcb)
    c.pack()
    maze_size = l.cget("text")
    print(maze_size)
    check = tk.BooleanVar()
    grid = numpy.array([[0] * maze_size] * maze_size)
    b = Button(root, text="Créer le Labyrinthe", pady=5, command=
    generate_maze(grid, maze_size, check))
    q = Button(root, text="Quitter", pady=5, command=root.quit)
    gap = 15
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1:
                canvas.create_rectangle(1 + gap * j, 1 + gap * i + 1, gap + gap * j + 1, gap + gap * i,
                                        outline="black", fill="#fb0")

    b.pack()
    q.pack()
    canvas.pack()
    root.mainloop()
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[i][j] > 0:
                grid[i][j] = 0
    distance(grid, maze_size)


def distance(grid, maze_size):
    grid[maze_size - 2][maze_size - 1] = 1
    k = 1
    while grid[1][1] == 0:
        for i in range(len(grid) - 2, 0, -1):
            for j in range(len(grid[i]) - 2, 0, -1):
                if grid[i][j] == 0:
                    if grid[i+1][j] > 0 or grid[i-1][j] > 0 or grid[i][j+1] > 0 or grid[i][j-1] > 0:
                        k += 1
                        grid[i][j] = k


def solveMaze(grid, maze_size):
    while grid[i][j] == grid[maze_size-2][maze_size-1]:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < grid[i+1][j] or grid[i][j] < grid[i-1][j] or grid[i][j] < grid[i][j+1] or \
                        grid[i][j] < grid[i][j-1]:
                    grid[i][j] = 0


if __name__ == '__main__':
    sizeerror = True
    erreurC = True
    complexe = False
    createLab()
    # while sizeerror:
    #     try:
    #         maze_size = int(input("Quelle taille de labyrinthe voulez vous ? Saisissez un taille impaire entre "
    #                               "10 et 50 : "))
    #         if 10 <= maze_size <= 50000 and maze_size % 2 == 1:
    #             sizeerror = False
    #             break
    #         print("La taille n'est pas valide !")
    #     except Exception:
    #         print("Veuillez mettre une bonne valeur !")
    # while erreurC:
    #     try:
    #         c = str(input("Le labyrinthe est-il complexe ? (o/n) : "))
    #         if c == 'o':
    #             complexe = True
    #             break
    #         elif c == 'n':
    #             complexe = False
    #             break
    #         print("Saisissez 'o' ou 'n' !")
    #     except Exception:
    #         print("Veuillez mettre 'o' ou 'n' !")
