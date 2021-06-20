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
    root.lift() #fenetre crée title labyrinthe taille 900x830 non modifiable,  decalage 320x0
    canvas = Canvas(root, height=1800, width=1080, scrollregion=(0, 0, 0, 0)) #cration zone de dessin du lab
    inputsize = 0
    created = False
    text = ''
    grid = None
    chkValue = tkinter.BooleanVar()
    chkValue.set(True)
    resolvable = False
    maze_size = None
    gap = 0
    pad = 0 #initialisation variables utilisé dans plusieurs fonctions

    def createLab(self): #création labyrinthe en fonction des entries de la fenetre
        self.canvas.delete("all") #nettoyage de la zone de dessin
        val = self.text.get()  #recuperation de la valeur de la zone de texte
        if val != '':
            try:
                self.maze_size = int(val)
                self.gap=(625/self.maze_size) #taille des cases en fonction de la taille du labyrinthe

                self.pad = (self.root.winfo_width()/2)-((self.maze_size*self.gap)/2) #decalage au mileu de la fenetre
                if self.maze_size != 0 and self.maze_size > 10 and self.maze_size < 150 and self.maze_size % 2 != 0: #si la taille du labyrinthe a taille correcte impaire et entre 10 et 150
                    self.created = True #nouveau labyrinthe créé
                    self.grid = numpy.array([[0] * self.maze_size] * self.maze_size) #création de la grille du labyrinthe
                    self.grid = main.generate_maze(self.grid, self.maze_size, self.chkValue.get()) #création du labyrinthe
                    for i in range(len(self.grid)): #pour chaque colonne et chaque ligne créer un carré de taille "self.gap" si la case est un mur (-1)
                        for j in range(len(self.grid[i])):
                            if (self.grid[i][j] == -1):
                                self.canvas.create_rectangle(self.pad + self.gap * j, 1 + self.gap * i, self.pad + self.gap + self.gap * j,
                                                             1 + self.gap + self.gap * i,
                                                             outline="black", fill="#fb0")
                                self.canvas.pack
            except:
                pass
    #createLab

    def resolveLab(self):
        if self.created: #si un nouveau labyrinthe a été créé et n'a pas été resolu
            self.created = False  #le résoudre et afficher le meilleur chemin trouvé
            self.grid = main.distance(self.grid, self.maze_size)
            self.solveMaze()


    def __init__(self):

        l = Label(self.root, text="Quelle taille de labyrinthe voulez vous ?\nSaisissez une taille impaire entre "
                                  "10 et 150 : ", pady=5)
        l.config(font=("Courier", 10), pady=5)
        l.pack() #zone de texte parlant de la taille du labyrinthe

        self.text = Entry(self.root, width=15)
        self.text.insert(0,"25")
        self.text.pack() #zone de texte pour l'utilisateur
        resolve = Button(self.root, text="Résoudre", pady=5, command=self.resolveLab) #bouton Résoudre
        q = Button(self.root, text="Quitter", pady=5, command=exit) #bouton quitter
        c = Checkbutton(self.root, text="Le Labyrinthe est-il complexe ?", pady=5, var=self.chkValue, state='normal') #bouton complexe ou non
        c.pack()

        b = Button(self.root, text="Créer le Labyrinthe", pady=5, command=self.createLab) #bouton créer le labyrinthe
        b.pack()
        resolve.pack()
        q.pack()
        self.canvas.pack()
        #pack (injection) des widgets sur la fenetre


    def changecell(self, x, y):
        #modifier les cases appelées en rouge (resolution du labyrinthe)
        self.canvas.create_rectangle(self.pad + self.gap * x, 1 + self.gap * y, self.pad + self.gap + self.gap * x, 1 + self.gap + self.gap * y,
                                     outline="black", fill="#8B0000")
        self.canvas.pack()
        self.root.update()
        time.sleep(0.04) #temps d'attente pour faire une animation de l'apparition du chemin

    def end(self):
        self.root.mainloop() #maintenir la fenetre ouverte et à l'ecoute des events (boutons)

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
