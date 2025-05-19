from tkinter import *

def my_function():
    my_label.config(text="Lubisz to!")


root  = Tk()
root.geometry("1200x760")
root.title("Map Book KF")



my_label = Label(root, text="Map Book KF")
my_label.grid(column=0, row=0)
my_button = Button(root, text="Like",command=my_function)
my_button.grid(column=1, row=1)

root.mainloop()




#ustawić kursor
#ALT
#KURSOR + ALT