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
        
#frame 1 ==============================================================================================================================================
        Label(self.f1,text="Name:").grid(row=1,column=1)
        Entry (self.f1,width=20).grid(row=1,column=2)
        Button(self.f1,text="Begin Order", command=self.beginorder).grid(columnspan=2,column=1)
#frame 2 ==============================================================================================================================================
        Button(self.f2,text="Cancel", command=self.cancel).grid()
        Button(self.f2,text="Continue", command=self.continueb).grid()
        Label(self.f2,text="Frame 2 ").grid()
        Button(self.f2,text="Drinks",command=self.drink).grid(row=1,column=2)
        Button(self.f2,text="Sandwhich",command=self.sandwich).grid(row=1,column=1)

        self.drinkframe = Frame(self.f2,bg="yellow",width=100,height=100)
        self.drinkframe.grid(pady=20,padx=20)
        self.sandwichframe = Frame(self.f2,bg="red",width=100,height=100)
        self.sandwichframe.grid(pady=20,padx=20)
        self.sandwichframe.grid_forget()
        
        self.drink=StringVar()
        self.drink.set(0)
        drink = ['Coke', 'Fanta', 'Pepsi']
        for item in drink:
            button1 = Checkbutton(self.drinkframe, bg="yellow",text=item,variable = self.drink, onvalue=item)
            button1.grid(padx=10)

        self.sandwich=StringVar()
        self.drink.set(0)
        sandwich = ['chicken', 'egg', 'ham']
        for item in sandwich:
            button2 = Checkbutton(self.sandwichframe, bg="red",text=item,variable = self.sandwich, onvalue=item)
            button2.grid(padx=10)

#frame 3 ==============================================================================================================================================
        Button(self.f3,text="Edit", command=self.edit).grid()
        Button(self.f3,text="Continue").grid()
        Label(self.f3,text="Frame 3 ").grid()
        self.listframe = Frame(self.f3,bg="grey",width=100,height=100)
        self.listframe.grid(pady=20,padx=20)
        self.text = Label(self.listframe, text=self.drink.get()+ self.sandwich.get() )
        self.text.grid()


    def sandwich(self):
        self.drinkframe.grid_forget()
        self.sandwichframe.grid() 
    def drink(self):
        self.sandwichframe.grid_forget()
        self.drinkframe.grid() 

    def continueb(self):
        self.f2.grid_forget()
        self.f3.grid()  
        self.text.configure(text=self.drink.get()+" "+ self.sandwich.get())
        self.text.grid()

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
root.geometry("200x200")
Cafe(root)
root.mainloop()