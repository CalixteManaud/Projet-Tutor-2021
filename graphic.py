import tkinter
from tkinter import *
import time

import numpy

import main
from main import *


class graphic():
    root = Tk()
    root.title("Labyrinthe")
    root.geometry("900x830+320+0")
    root.resizable(False, False)
    root.lift()
    canvas = Canvas(root, height=1800, width=1080, scrollregion=(0, 0, 0, 0))
    inputsize = 0
    created = False
    text = ''
    grid = None
    chkValue = tkinter.BooleanVar()
    chkValue.set(True)
    resolvable = False
    maze_size = None
    gap = 0
    pad = 0

    def setInputSize(self):
        self.canvas.delete("all")
        val = self.text.get()
        if val != '':
            print("e")
            try:
                self.maze_size = int(val)
                self.gap=(625/self.maze_size)

                self.pad = (self.root.winfo_width()/2)-((self.maze_size*self.gap)/2)
                if self.maze_size != 0 and self.maze_size > 10 and self.maze_size < 150 and self.maze_size % 2 != 0:
                    self.created = True
                    self.grid = numpy.array([[0] * self.maze_size] * self.maze_size)
                    self.grid = main.generate_maze(self.grid, self.maze_size, self.chkValue.get())
                    for i in range(len(self.grid)):
                        for j in range(len(self.grid[i])):
                            if (self.grid[i][j] == -1):
                                self.canvas.create_rectangle(self.pad + self.gap * j, 1 + self.gap * i, self.pad + self.gap + self.gap * j,
                                                             1 + self.gap + self.gap * i,
                                                             outline="black", fill="#fb0")
                                self.canvas.pack
            except:
                pass

    def resolveLab(self):
        if self.created:
            self.created = False
            print("e")
            self.grid = main.distance(self.grid, self.maze_size)
            self.solveMaze()


    def __init__(self):

        l = Label(self.root, text="Quelle taille de labyrinthe voulez vous ?\nSaisissez une taille impaire entre "
                                  "10 et 150 : ", pady=5)
        l.config(font=("Courier", 10), pady=5)
        l.pack()

        self.text = Entry(self.root, width=15)
        self.text.pack()
        resolve = Button(self.root, text="Résoudre", pady=5, command=self.resolveLab)
        q = Button(self.root, text="Quitter", pady=5, command=exit)
        c = Checkbutton(self.root, text="Le Labyrinthe est-il complexe ?", pady=5, var=self.chkValue, state='normal')
        c.pack()

        b = Button(self.root, text="Créer le Labyrinthe", pady=5, command=self.setInputSize)
        b.pack()
        resolve.pack()
        q.pack()
        self.canvas.pack()


    def changecell(self, x, y):

        self.canvas.create_rectangle(self.pad + self.gap * x, 1 + self.gap * y, self.pad + self.gap + self.gap * x, 1 + self.gap + self.gap * y,
                                     outline="black", fill="#8B0000")
        self.canvas.pack()
        self.root.update()
        time.sleep(0.01)

    def end(self):
        self.root.mainloop()

    def solveMaze(self):
        x = 1
        y = 1
        self.changecell(0, 1)
        self.changecell(y, x)
        while x != self.maze_size - 1 and y != self.maze_size - 1:
            if self.grid[x][y] >= self.grid[x + 1][y] > 0:
                self.grid[x][y] = 0
                x += 1
                self.changecell(y, x)
            elif self.grid[x][y] >= self.grid[x - 1][y] > 0:
                self.grid[x][y] = 0
                x -= 1
                self.changecell(y, x)
            elif self.grid[x][y] >= self.grid[x][y - 1] > 0:
                self.grid[x][y] = 0
                y -= 1
                self.changecell(y, x)
            elif self.grid[x][y] >= self.grid[x][y + 1] > 0:
                self.grid[x][y] = 0
                y += 1
                self.changecell(y, x)
        self.grid[1][0] = 0
        self.grid[self.maze_size - 2][self.maze_size - 1] = 0
