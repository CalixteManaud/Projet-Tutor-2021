from tkinter import *

class graphic():

    root = Tk()
    root.title("Labyrinthe")
    root.geometry("1920x1080")
    root.attributes('-fullscreen', True)
    root.lift()
    canvas = Canvas(root, height=1800, width=1080, scrollregion=(0, 0, 0, 0))

    def __init__(self, grid):

        hbar = Scrollbar(self.root, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(self.root, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        l = Label(self.root, text="Quelle taille de labyrinthe voulez vous ?\nSaisissez une taille impaire entre "
                             "10 et 50 : ", pady=5)
        l.config(font=("Courier", 10), pady=5)
        text = Entry(self.root, width=15)
        t = Text(self.root, height=2, width=10)
        l.pack()
        text.pack()
        t.pack
        c = Checkbutton(self.root, text="Le Labyrinthe est-il complexe ?", pady=5)
        c.pack()
        b = Button(self.root, text="Créer le Labyrinthe", pady=5)
        q = Button(self.root, text="Quitter", pady=5, command=self.root.quit)
        gap = 15
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == -1):
                    self.canvas.create_rectangle(307 + gap * j, 1 + gap * i , 307 + gap + gap * j, 1 + gap + gap * i,
                                            outline="black", fill="#fb0")
        b.pack()
        q.pack()
        self.canvas.pack()
        self.root.update()

    def changecell(self, x, y):

        gap = 15
        self.canvas.create_rectangle(307 + gap * x, 1 + gap * y, 307 + gap + gap * y, 1 + gap + gap * x,
                                outline="black", fill="#8B0000")
        self.canvas.pack()
        self.root.update()
        pass

    def end(self):
        self.root.mainloop()