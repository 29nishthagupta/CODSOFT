from tkinter import *
root = Tk()

root.geometry("500x550+400+40")
root.resizable(False, False)
root.configure(background="#9ED2BE")


root.title("Calculater")

e =Entry(root, width=75, borderwidth=10, bg="white")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


Image_icon = PhotoImage(file="calculator.png")
root.iconphoto(FALSE, Image_icon)



def button_clear():
    e.delete(0, END)


def button_add():
    first_number =e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        result = f_num + float(second_number)
    elif math == "subtraction":
        result = f_num - float(second_number)
    elif math == "multiply":
        result = f_num * float(second_number)
    elif math == "division":
        result = f_num / float(second_number)
    elif math == "percentage":
        result = f_num * (float(second_number) / 100)
    e.insert(0, result)



def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)


def button_per():
    second_number = e.get()
    e.delete(0, END)
    result = f_num * (float(second_number) / 100)
    e.insert(0, result)


def button_click(number):

    # Check if the clicked number is a decimal point
    if number == ".":
        if "." not in e.get():
            e.insert(END, ".")
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))


def button_cross():
    e.delete(0)

# Define Button
button_1 = Button(root, text="1", padx=40, pady=20, font="lucida 15 bold", bg="#35A29F", command=lambda :button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,font="lucida 15 bold",bg="#35A29F", command=lambda :button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,font="lucida 15 bold",bg="#35A29F", command=lambda :button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F", command=lambda :button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, font="lucida 15 bold", bg="#35A29F",command=button_add)
button_equal = Button(root, text="=", padx=40, pady=20, font="lucida 15 bold",bg="#159895", command=button_equal)
button_clear = Button(root, text="Clear", padx=80, pady=20, font="lucida 15 bold",bg="#FFD93D",command=button_clear)
button_sub = Button(root, text="-", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=button_sub)
button_div = Button(root, text="/", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=button_div)
button_mul = Button(root, text="*", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=button_multiply)
button_per = Button(root, text="%", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=button_per)
button_dot = Button(root, text=".", padx=40, pady=20, font="lucida 15 bold",bg="#35A29F",command=lambda :button_click("."))
button_cross = Button(root, text="x", padx=40, pady=20, font="lucida 15 bold",bg="#FE0000",command=button_cross)

# put button on screen

button_1.grid(row=3, column=0, pady=10)
button_2.grid(row=3, column=1, pady=10)
button_3.grid(row=3, column=2, pady=10)
button_4.grid(row=2, column=0, pady=10)
button_5.grid(row=2, column=1, pady=10)
button_6.grid(row=2, column=2, pady=10)
button_7.grid(row=1, column=0, pady=10)
button_8.grid(row=1, column=1, pady=10)
button_9.grid(row=1, column=2, pady=10)
button_0.grid(row=4, column=0, pady=10)
button_clear.grid(row=5, column=0, pady=10, columnspan=2)
button_add.grid(row=1, column=3, pady=10)
button_equal.grid(row=5, column=3, pady=10)
button_sub.grid(row=2, column=3, pady=10)
button_div.grid(row=3, column=3, pady=10)
button_mul.grid(row=4, column=3, pady=10)
button_per.grid(row=4, column=2, pady=10)
button_dot.grid(row=4, column=1, pady=10)
button_cross.grid(row=5, column=2, pady=10)

root.mainloop()