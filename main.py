import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for lts in range(randint(8, 10))]
    password_list += [choice(symbols) for sbs in range(randint(2, 4))]
    password_list += [choice(numbers) for nums in range(randint(2, 4))]

    shuffle(password_list)

    pw.insert(0, "".join(password_list))
    pyperclip.copy("".join(password_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {
        site.get(): {
            "email": mail.get(),
            "password": pw.get()
        }
    }

    if len(site.get()) > 0 and len(pw.get()) > 0:
        try:
            with open("data.json", 'r') as f:
                data = json.load(f)
                data.update(new_data)
            with open("data.json", 'w') as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            with open("data.json", 'w') as f:
                json.dump(new_data, f, indent=4)
        finally:
            site.delete(0, END)
            pw.delete(0, END)

    else:
        messagebox.showerror(title="Error", message="Please provide all the information")


# ---------------------------- FIND WEBSITE --------------------------- #

def search():
    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
            search_mail = data[site.get()]["email"]
            search_pw = data[site.get()]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No details for {site.get()}")
    else:
        messagebox.showinfo(title="Website Info", message=f"{site.get()}\nEmail: {search_mail}\nPassword: {search_pw}")


# ---------------------------- UI SETUP ------------------------------- #


FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=img)
canvas.grid(column=1, row=0)

site_l = Label(text="Website")
site_l.grid(column=0, row=1)

site = Entry(width=21)
site.focus()
site.grid(column=1, row=1)

search = Button(text="Search", command=search, width=13)
search.grid(column=2, row=1)

mail_l = Label(text="Email/Username")
mail_l.grid(column=0, row=2)

mail = Entry(width=38)
mail.insert(0, "samuelrivba@gmail.com")
mail.grid(column=1, row=2, columnspan=2)

pw_l = Label(text="Password")
pw_l.grid(column=0, row=3)

pw = Entry(width=21)
pw.grid(column=1, row=3)

gen = Button(text="Generate Password", command=gen_pw)
gen.grid(column=2, row=3)

add = Button(text="Add", command=save, width=36)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
