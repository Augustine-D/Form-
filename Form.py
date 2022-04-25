
from tkinter import *
from turtle import bgcolor

screen = Tk()
screen.geometry("500x500")
screen.title("PYTHOM FORM TO TEXT FILE")
screen.configure(bg="#D8D8D8")
heading = Label(text="PYTHOM FORM TO TEXT FILE", bg="#34495E",
                fg="#f2f2f2", width="500", height="2")
heading.pack()


def save_info():
    firstname_info = Firstname.get()
    lastname_info = Lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info, lastname_info, age_info)

    file = open("user.txt", "w")
    file.write(firstname_info)
    file.write(lastname_info)
    file.write(age_info)
    file.close()
    print("User ", firstname_info, "has been registered")

    Firstname_entry.delete(0, END)
    Lastname_entry.delete(0, END)
    age_entry.delete(0, END)


def change_color():
    Label.config(bg="#D8D8D8", fg="white")


firstname_text = Label(text="Firstname* ", )
lastname_text = Label(text="Lastname* ", )
age_text = Label(text="Age* ",)

firstname_text.place(relx=0.5, rely=0.1, anchor=CENTER)
lastname_text.place(relx=0.5, rely=0.2, anchor=CENTER)
age_text.place(relx=0.5, rely=0.3, anchor=CENTER)

Firstname = StringVar()
Lastname = StringVar()
age = IntVar()


Firstname_entry = Entry(textvariable=Firstname, width="50")
Lastname_entry = Entry(textvariable=Lastname, width="50")
age_entry = Entry(textvariable=age, width="50")

Firstname_entry.place(relx=0.5, rely=0.15, anchor=CENTER)
Lastname_entry.place(relx=0.5, rely=0.25, anchor=CENTER)
age_entry.place(relx=0.5, rely=0.35, anchor=CENTER)


register = Button(text="Register", width="30",
                  command=save_info, background="#34C487")
register.place(relx=0.5, rely=0.45, anchor=CENTER)

screen.mainloop()
