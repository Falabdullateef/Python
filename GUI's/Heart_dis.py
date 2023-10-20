# unfinished project
# I dont plan on finishing it because I have a better version of it.
# Here is the link: https://github.com/Falabdullateef/Java/tree/main/Biology/Heart%20disease%20survey

from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Create an instance of tkinter frame
root = Tk()

root.geometry("1080x900")
root.config(background='black')

def nothing():
    return 0

Gquestion = Label(text="What is your gender?", font=("bold", 30), pady=10, foreground="#03fc30", background="black")
Gquestion.pack()

Gvar = IntVar()

male = Radiobutton(root,
                   text="Male",
                   variable=Gvar,
                   font=("bold", 20),
                   value=1,
                   foreground="red",
                   background="black",
                   activebackground="#03fc30",
                   command=nothing,
                   pady=20)
male.pack(anchor=W)

female = Radiobutton(root,
                     text="Female",
                     variable=Gvar,
                     value=2,
                     foreground="red",
                     background="black",
                     font=("bold", 20),
                     activebackground="#03fc30",
                     command=nothing,
                     pady=10)
female.pack(anchor=W)

Squestion = Label(text="Have you ever smoked?", font=("bold", 30), pady=10, foreground="#03fc30", background="black")
Squestion.pack()

Svar=IntVar

Yes = Radiobutton(root,
                  text="Yes",
                  variable=Svar,
                  font=("bold", 20),
                  value=1,
                  foreground="red",
                  background="black",
                  activebackground="#03fc30",
                  command=nothing,
                  pady=20)
Yes.pack(anchor=W)

No = Radiobutton(root,
                 text="No",
                 variable=Svar,
                 font=("bold", 20),
                 value=1,
                 foreground="red",
                 background="black",
                 activebackground="#03fc30",
                 command=nothing,
                 pady=20)
No.pack(anchor=W)

root.mainloop()
