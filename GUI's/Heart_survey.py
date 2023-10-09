from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create an instance of tkinter frame
root = Tk()

root.geometry("1200x300")
root.config(background='black')
root.resizable(0, 0)

def heartdisQ():
    def sel():
        selection = str(var.get())
        if selection == str(0):
            messagebox.showinfo("No choice", "Please choose one of the options to move to the next question")
        elif selection == str(1):
            print("Has had a heart disease")
            messagebox.showinfo("Finished", "You have finished the survey thank you for sharing you participating.")
            quit()
        elif selection == str(2):
            messagebox.showinfo("Finished", "You have finished the survey thank you for sharing you participating.")
            print("Has not had a heart disease")
            quit()

    question = Label(text="Have you ever had a heart disease?", font=("bold", 30), pady=10, foreground="#03fc30",
                     background="black")
    question.pack()

    var = IntVar()

    Yes = Radiobutton(root,
                      text="Yes",
                      variable=var,
                      font=("bold", 20),
                      value=1,
                      foreground="red",
                      background="black",
                      activebackground="#03fc30",
                      pady=20)
    Yes.pack(anchor=W)

    No = Radiobutton(root,
                     text="No",
                     variable=var,
                     value=2,
                     foreground="red",
                     background="black",
                     font=("bold", 20),
                     activebackground="#03fc30",
                     pady=10)
    No.pack(anchor=W)

    submit = Button(root,
                    text="Submit",
                    font=("bold", 20),
                    foreground="#03fc30",
                    background="black",
                    activebackground="#ab1b20",
                    command=sel)
    submit.pack(anchor=CENTER)

def smokeQ():
    def sel():
        selection = str(var.get())
        if selection == str(0):
            messagebox.showinfo("No choice", "Please choose one of the options to move to the next question")
        elif selection == str(1):
            print("Has smoked")
            Yes.destroy()
            No.destroy()
            question.destroy()
            submit.destroy()
            heartdisQ()
        elif selection == str(2):
            print("Has not smoked")
            Yes.destroy()
            No.destroy()
            question.destroy()
            submit.destroy()
            heartdisQ()

    question = Label(text="Have you ever smoked?", font=("bold", 30), pady=10, foreground="#03fc30", background="black")
    question.pack()

    var = IntVar()

    Yes = Radiobutton(root,
                      text="Yes",
                      variable=var,
                      font=("bold", 20),
                      value=1,
                      foreground="red",
                      background="black",
                      activebackground="#03fc30",
                      pady=20)
    Yes.pack(anchor=W)

    No = Radiobutton(root,
                     text="No",
                     variable=var,
                     value=2,
                     foreground="red",
                     background="black",
                     font=("bold", 20),
                     activebackground="#03fc30",
                     pady=10)
    No.pack(anchor=W)

    submit = Button(root,
                    text="Submit",
                    font=("bold", 20),
                    foreground="#03fc30",
                    background="black",
                    activebackground="#ab1b20",
                    command=sel)
    submit.pack(anchor=CENTER)


def genderQ():
    def sel():
        Gender_selection = str(var.get())
        if Gender_selection == str(0):
            messagebox.showinfo("No choice", "Please choose one of the options to move to the next question")
        elif Gender_selection == str(1):
            print("Gender: Male")
            question.destroy()
            male.destroy()
            female.destroy()
            submit.destroy()
            smokeQ()
        elif Gender_selection == str(2):
            print("Gender: Female")
            question.destroy()
            male.destroy()
            female.destroy()
            submit.destroy()
            smokeQ()


    question = Label(text="What is your gender?", font=("bold", 30), pady=10, foreground="#03fc30", background="black")
    question.pack()

    var = IntVar()

    male = Radiobutton(root,
                       text="Male",
                       variable=var,
                       font=("bold", 20),
                       value=1,
                       foreground="red",
                       background="black",
                       activebackground="#03fc30",
                       pady=20)
    male.pack(anchor=W)

    female = Radiobutton(root,
                         text="Female",
                         variable=var,
                         value=2,
                         foreground="red",
                         background="black",
                         font=("bold", 20),
                         activebackground="#03fc30",
                         pady=10)
    female.pack(anchor=W)

    submit = Button(root,
                    text="Submit",
                    font=("bold", 20),
                    foreground="#03fc30",
                    background="black",
                    activebackground="#ab1b20",
                    command=sel)
    submit.pack(anchor=CENTER)


def submitcheck():
    name = name_entry.get()
    if name == "":
        messagebox.showinfo('Submission error', "Please enter your first and last name to continue to the survey")
    else:
        print("Name: " + name)
        name_entry.destroy()
        title.destroy()
        welcome.destroy()
        welcome2.destroy()
        imready.destroy()
        clear_button.destroy()
        genderQ()


def clear():
    name_entry.delete(0, END)
    return 0


# name entry

name_entry = Entry(bg="#03fc30", font=("bold", 20), width=30)
name_entry.place(x=35, y=200)

# Welcome message
title = Label(text="Heart disease survey", font=("bold", 30), pady=35, padx=35, foreground="#03fc30",
              background="black")
title.pack()

welcome = Label(text="Welcome to the heart disease survey, made by the saudi ministry of health.", font=("bold", 20),
                padx=35, foreground="#03fc30", background="black")
welcome.pack()

welcome2 = Label(text="First start by entering your first and second name. Once you are ready simply click I'm ready.",
                 font=("bold", 20), padx=35, foreground="#03fc30", background="black")
welcome2.pack(anchor=W)

imready = Button(text="I'm ready", font=("bold", 15), bg="#05fafa", width=15, height=1,
                 activebackground="#03fc30", activeforeground="black", command=submitcheck)
imready.place(x=700, y=197)

clear_button = Button(text="Clear text", font=("bold", 15), bg="#fa0505", height=1, width=15, fg="blue", command=clear)
clear_button.place(x=510, y=198)

root.mainloop()

root.geometry("550x350")

root.mainloop()

#export the data to a csv file
import csv

