import pickle
from tkinter.font import Font
from tkinter import filedialog, messagebox
from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("500x600+400+40")
root.resizable(False, False)
root.configure(background="#FBD85D")


task_list = []
# icon

Image_icon = PhotoImage(file="to-do-list.png")
root.iconphoto(FALSE, Image_icon)



# text

my_text = Label(root, text="Things To Do", font=("Times", 40), fg="#6C3428", bg="#FFDBAA")
my_text.pack(pady=40)

my_font = Font(
    family="Times",
    size=28,
    weight="bold"
)

# create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# create listbox

my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="#FFDBAA",
                  bd=0,
                  fg="#6C3428",
                  highlightthickness=0,
                  selectbackground="#F1C27B",
                  activestyle="none"
                  )
my_list.pack(side=LEFT, fill=BOTH)
# create dummy list
stuff = ["Walk the dog", "Wake up 6AM","Buy some milk"]
# Add dummy list to list box

for items in stuff:
    my_list.insert(END, items)

# create scroll bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create entry box to add items to the list

my_entry = Entry(root, font=("Helvetica", 24), width=25)
my_entry.pack(pady=20)

# create a button frame

button_frame = Frame(root)
button_frame.pack(pady=20)


# functions

def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_off_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")

    # get rid off selection bar
    my_list.selection_clear(0, END)


def uncross_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # get rid off selection bar
    my_list.selection_clear(0, END)


def delete_cross_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def Save_list():
    file_name = filedialog.asksaveasfilename(defaultextension=".dat", filetypes=[("DAT files", "*.dat")])
    if file_name:

        if file_name.endswith(".dat"):
            pass
            # Perform the desired save operation here
        else:
            messagebox.showerror("Invalid File Name", "Please select a .dat file for saving.")

            # delete crossed items before save
        count = 0
        while count < my_list.size():

            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1
                # grab all the stuff from the list
            stuff = my_list.get(0, END)

            # open the file
            output_file = open(file_name, 'wb')

            # add the stuff to the file
            pickle.dump(stuff, output_file)


def Open_list():
    file_name = filedialog.askopenfilename(
        initialdir="D:\\Users\\Bhumi\\PycharmProjects\\codsoft projects\\Data",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"),
                   ("All Files", "*.*")))

    if file_name:
        # delete currently open list
        my_list.delete(0, END)

        # open file
        input_file = open(file_name, 'rb')
        # load the data from the file
        stuff = pickle.load(input_file)

        # output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)


def Clear_list():
    my_list.delete(0, END)


# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# add drop down items
file_menu.add_command(label="Save List", command=Save_list)
file_menu.add_command(label="Open List", command=Open_list)
file_menu.add_separator()

file_menu.add_command(label="Clear List", command=Clear_list)

# add some button
delete_button = Button(button_frame, text="Delete Item",  font=("Times", 12), fg="white", bg="#6C3428",command=delete_item)
Add_button = Button(button_frame, text="Add Item", font=("Times", 12), fg="white", bg="#6C3428",command=add_item)
cross_off_button = Button(button_frame, text="Cross off Item",  font=("Times", 12),fg="white", bg="#6C3428",command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", font=("Times", 12), fg="white", bg="#6C3428",command=uncross_item)
delete_cross_button = Button(button_frame, text="Delete Crossed ", font=("Times", 12),fg="white", bg="#6C3428",command=delete_cross_item)

delete_button.grid(row=0, column=0)
Add_button.grid(row=0, column=1)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3)
delete_cross_button.grid(row=0, column=4)

root.mainloop()
