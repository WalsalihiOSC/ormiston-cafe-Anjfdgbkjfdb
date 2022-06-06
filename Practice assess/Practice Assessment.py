from tkinter import *

class Cafe:
    def __init__(self, parent):
        self.f1 = Frame(parent)
        self.f1.grid()

        self.f2 = Frame(parent)
        self.f2.grid()
        self.f2.grid_forget()

        self.f3 = Frame(parent)
        self.f3.grid()
        self.f3.grid_forget()

        Label(self.f1,text="Name ").grid()
        Entry (self.f1,width=20).grid()
        Button(self.f1,text="Begin Order", command=self.beginorder).grid()

        Button(self.f2,text="Cancel", command=self.cancel).grid()
        Button(self.f2,text="Continue", command=self.continueb).grid()
        Label(self.f2,text="Frame 2 ").grid()


        Button(self.f3,text="Edit", command=self.edit).grid()
        Button(self.f3,text="Continue").grid()
        Label(self.f3,text="Frame 3 ").grid()


    def continueb(self):
        self.f2.grid_forget()
        self.f3.grid()  

    def edit(self):
        self.f3.grid_forget()
        self.f2.grid()

    def cancel(self):
        self.f2.grid_forget()
        self.f1.grid()


    def beginorder(self):
        self.f1.grid_forget()
        self.f2.grid()


root = Tk()
Cafe(root)
root.mainloop()