from tkinter import *
from tkinter import ttk

y = 0
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)

def quiz(y):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")

    Label(frame1, text="Total keyword in python ?", font=("Arial",30, "bold")).grid(row=2, column=2)
    Button(frame1, text="33", font=("Arial", 30, "bold"), bg="cyan",command=a_correct).grid(row=3,column=2)
    Button(frame1, text="30", font=("Arial", 30, "bold"), bg="cyan", command=a_wrong).grid(row=4,column=2)
    Button(frame1, text="31", font=("Arial", 30, "bold"), bg="cyan", command=a_wrong).grid(row=5,column=2)


    Label(frame2, text="Output of 2**3 ?", font=("Arial",30, "bold")).grid(row=2, column=2)
    Button(frame2, text="3", font=("Arial", 30, "bold"), bg="cyan",command=a2_wrong).grid(row=3,column=2)
    Button(frame2, text="4", font=("Arial", 30, "bold"), bg="cyan", command=a2_wrong).grid(row=4,column=2)
    Button(frame2, text="8", font=("Arial", 30, "bold"), bg="cyan", command=a2_correct).grid(row=5,column=2)

    Label(frame3, text="Which is Keyword in python ?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame3, text="def", font=("Arial", 30, "bold"), bg="cyan",command=a3_correct).grid(row=3, column=2)
    Button(frame3, text="int", font=("Arial", 30, "bold"), bg="cyan", command=a3_wrong).grid(row=4, column=2)
    Button(frame3, text="str", font=("Arial", 30, "bold"), bg="cyan",command=a3_wrong).grid(row=5, column=2)

    Label(frame4, text="How Tuple is denoted ?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame4, text="{}", font=("Arial", 30, "bold"), bg="cyan", command=a4_wrong).grid(row=3, column=2)
    Button(frame4, text="()", font=("Arial", 30, "bold"), bg="cyan",command=a4_correct).grid(row=4, column=2)
    Button(frame4, text="[]", font=("Arial", 30, "bold"), bg="cyan",command=a4_wrong).grid(row=5, column=2)

    Label(frame5, text="List is stored in ?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame5, text="{}", font=("Arial", 30, "bold"), bg="cyan",command=a5_wrong).grid(row=3, column=2)
    Button(frame5, text="()", font=("Arial", 30, "bold"), bg="cyan",command=a5_wrong).grid(row=4, column=2)
    Button(frame5, text="[]", font=("Arial", 30, "bold"), bg="cyan",command=a5_correct).grid(row=5, column=2)


def a_correct():
    Label(frame1, text="Correct", font=("Arial", 20,"bold"),bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame1, text="Marks Obtain: 1", font=("Arial", 20,"bold"),bg="black", fg="white").grid(row=1, column=2)


def a_wrong():
    Label(frame1, text="Incorrect", font=("Arial", 20, "bold"), bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame1, text="Marks Obtain: 0", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=2)


def a2_correct():
    Label(frame2, text="Correct", font=("Arial", 20,"bold"),bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame2, text="Marks Obtain: 1", font=("Arial", 20,"bold"),bg="black", fg="white").grid(row=1, column=2)

def a2_wrong():
    Label(frame2, text="Incorrect", font=("Arial", 20, "bold"), bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame2, text="Marks Obtain: 0", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=2)


def a3_correct():
    Label(frame3, text="Correct", font=("Arial", 20,"bold"),bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame3, text="Marks Obtain: 1", font=("Arial", 20,"bold"),bg="black", fg="white").grid(row=1, column=2)

def a3_wrong():
    Label(frame3, text="Incorrect", font=("Arial", 20, "bold"), bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame3, text="Marks Obtain: 0", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=2)


def a4_correct():
    Label(frame4, text="Correct", font=("Arial", 20,"bold"),bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame4, text="Marks Obtain: 1", font=("Arial", 20,"bold"),bg="black", fg="white").grid(row=1, column=2)


def a4_wrong():
    Label(frame4, text="Incorrect", font=("Arial", 20, "bold"), bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame4, text="Marks Obtain: 0", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=2)

def a5_correct():
    Label(frame5, text="Correct", font=("Arial", 20,"bold"),bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame5, text="Marks Obtain: 1", font=("Arial", 20,"bold"),bg="black", fg="white").grid(row=1, column=2)


def a5_wrong():
    Label(frame5, text="Incorrect", font=("Arial", 20, "bold"), bg="green", fg="yellow").grid(row=1, column=1)
    Label(frame5, text="Marks Obtain: 0", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=2)


quiz(y)
a.pack()

root.mainloop()
