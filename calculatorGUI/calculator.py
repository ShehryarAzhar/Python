from tkinter import *

# Main Window 
root = Tk()
root.title("Calculator")

# input field
e = Entry(root, width=23)
e.grid(row=0, column=0, columnspan=4)


# BUTTON FUNCTIONS
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    
    global f_num, math
    f_num = int(first_number)
    math = "addition"

    e.delete(0, END)


def subt():
    first_number = e.get()
    
    global f_num, math
    f_num = int(first_number)
    math = "subtraction"

    e.delete(0, END)

def mult():
    first_number = e.get()
    
    global f_num, math
    f_num = int(first_number)
    math = "multiplication"

    e.delete(0, END)

def div():
    first_number = e.get()
    
    global f_num, math
    f_num = int(first_number)
    math = "division"

    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))
        

# define buttons
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=20, pady=20, command=add)
button_subt = Button(root, text="-", padx=20, pady=20, command=subt)
button_mult = Button(root, text="x", padx=20, pady=20, command=mult)
button_div = Button(root, text="/", padx=22, pady=20, command=div)

button_equal = Button(root, text="=", padx=47, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=90, pady=20, command=clear)

# display buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subt.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

# display Main Window
root.mainloop()