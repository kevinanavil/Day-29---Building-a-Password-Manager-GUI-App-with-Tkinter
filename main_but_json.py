import tkinter
import pandas
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen():

    pass_entry.delete(0, tkinter.END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    #Because shuffle return none type
    password = ''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    web_fill = web_entry.get()
    email_fill = email_entry.get()
    pass_fill = pass_entry.get()
    new_data = {
        web_fill:{
            "email": email_fill,
            "password": pass_fill
        }
    }

    if len(web_fill) == 0 or len(pass_fill) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave filed empty")
    else:
        try:
            with open("data_base.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)

        except:
            data = {}

        #update old data
        data.update(new_data)

        with open("data_base.json", "w") as data_file:
            #saving updated data
            json.dump(data, data_file, indent=4)

        web_entry.delete(0, tkinter.END)
        pass_entry.delete(0, tkinter.END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():

    pass_entry.delete(0, tkinter.END)
    web_fill = web_entry.get()

    if len(web_fill) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave filed empty")
    else:
        try:
            with open("data_base.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except:
            messagebox.showinfo(title="Error", message="Don't have data")
        else:
            if web_fill in data:
                email_info = data[web_fill]["email"]
                pass_info = data[web_fill]["password"]
                messagebox.showinfo(title=web_fill, message=f"Email: {email_info}\nPassword: {pass_info}") 
            else:
                messagebox.showinfo(title="Error", message="Don't have data")                                
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
picture = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(row=0, column=1)

web_text = tkinter.Label(text="Website:")
web_text.grid(row=1, column=0)
email_text = tkinter.Label(text="Email/Username:")
email_text.grid(row=2, column=0)
pass_text = tkinter.Label(text="Password:")
pass_text.grid(row=3, column=0)

web_entry = tkinter.Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = tkinter.Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kev514020@gmail.com")
pass_entry = tkinter.Entry(width=33)
pass_entry.grid(row=3, column=1)

search_button = tkinter.Button(text="Search", command=search, width=15)
search_button.grid(row=1, column=2)
gen_button = tkinter.Button(text="Generate Password", command=gen)
gen_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", command=add, width=44)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()