from tkinter import *
import tkinter as tk



class Example(Frame):


    def createTextBox(self, root):

        canvas = Canvas(root)

        l = Label(root, text="Quelle taille de labyrinthe voulez vous ?\nSaisissez un taille impaire entre "
                                  "10 et 50 : ", pady=5)
        l.config(font=("Courier", 10), pady=5)

        b = Button(root, text = "Créer le Labyrinthe", pady=5)
        c = Checkbutton(root, text="Le Labyrinthe est-il complexe ?", pady=5)

        canvas.create_rectangle(30, 10, 50, 50,
                                outline="#fb0", fill="#fb0")

        l.pack()
        c.pack()
        b.pack()
        canvas.pack()




        tk.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title("Labyrinthe")
    root.geometry("500x250")

    ex = Example(root)
    ex.createTextBox(root)
    root.mainloop()