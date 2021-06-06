from tkinter import *

class Table:

    def __init__(self, root):

        # code for creating table
        total_rows=49
        total_columns=30
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=1, fg='black', #fg : color text; width : taille case
                               font=('Arial', 16, 'bold'), bd=0, relief='flat', bg='black') #bd:borderwidth
                self.e.grid(row=i, column=j)
                self.e.insert(END, '█')

    def changecell(self, root, row, column, wall):

        if wall: self.e = Entry(root, width=1, fg='white', font=('Arial', 12, 'bold'),
                                bd=0, relief='flat', bg='white')
        if not wall: self.e = Entry(root, width=1, fg='black', font=('Arial', 12, 'bold'), bd=0, relief='flat',
                                    bg='black')
        self.e.delete(0,"end")
        self.e.grid(row=row, column=column)
        self.e.insert(END, '█')