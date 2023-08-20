from tkinter import *
from random import randint
root = Tk()

root.geometry("440x300+400+40")
root.resizable(False, False)
root.configure(background="#D8D9DA")


root.title("Password generator")

Image_icon = PhotoImage(file="lock.png")
root.iconphoto(FALSE, Image_icon)

my_password = chr(randint(33,126))

#functions

# Generate random Strong password
def new_rand():
    # clear our Entry box
    pw_entry.delete(0, END)

    # get pw length and convert to integer
    pw_length = int(my_entry.get())

    # create a variable to hold our password

    my_password = ''

    # loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # output password to the screen
    pw_entry.insert(0, my_password)

# copy to clipboard
def clipper():
    # clear clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(pw_entry.get())


# Label frame
label_frame = LabelFrame(root, text="How many character you want?" )
label_frame.pack(pady=20)

#create Entry Box To designate Number of Character
my_entry = Entry(label_frame, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#create Entry Box for our returned password
pw_entry = Entry(root, text='', font=("Helvetica",24), bd=0, bg="#D8D9DA")
pw_entry.pack(pady=20)

# create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#create button
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=1,padx=10,pady=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=2, padx=10, pady=10)



root.mainloop()