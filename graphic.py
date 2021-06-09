from tkinter import *


def lab(grid):

    root = Tk()
    root.title("Labyrinthe")
    root.geometry("1920x1080")
    root.attributes('-fullscreen', True)
    root.lift()
    canvas = Canvas(root, height=1800, width=1080, scrollregion=(0, 0, 0, 0))
    hbar = Scrollbar(root, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=canvas.xview)
    vbar = Scrollbar(root, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    l = Label(root, text="Quelle taille de labyrinthe voulez vous ?\nSaisissez une taille impaire entre "
                         "10 et 50 : ", pady=5)
    l.config(font=("Courier", 10), pady=5)
    text = Entry(root, width=15)
    t = Text(root, height=2, width=10)
    l.pack()
    text.pack()
    t.pack
    c = Checkbutton(root, text="Le Labyrinthe est-il complexe ?", pady=5)
    c.pack()
    b = Button(root, text="Créer le Labyrinthe", pady=5)
    q = Button(root, text="Quitter", pady=5, command=root.quit)
    gap = 15
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == -1):
                canvas.create_rectangle(307 + gap * j, 1 + gap * i , 307 + gap + gap * j, 1 + gap + gap * i,
                                        outline="black", fill="#fb0")
    b.pack()
    q.pack()
    canvas.pack()
    root.mainloop()
