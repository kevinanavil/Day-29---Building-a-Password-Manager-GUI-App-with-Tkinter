import tkinter
import pandas
from tkinter import messagebox
import random
import pyperclip
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

    data = pandas.DataFrame([[web_fill, email_fill, pass_fill]], columns=["Website", "Email/Username", "Password"])

    if len(web_fill) == 0 or len(pass_fill) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave filed empty")

    else:
        is_ok = messagebox.askokcancel(title=web_fill, message=f"Email: {email_fill}\nPassword: {pass_fill}\nIs it OK to save?")

        if is_ok:
            with open("data_base.csv", "a", newline='') as data_file:
                # data.write(f"{web_fill}\t{email_fill}\t{pass_fill}\n")  
                data.to_csv(data_file, header=(not data_file.tell()), index=False, mode='a')
                web_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)
        
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

web_entry = tkinter.Entry(width=52)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = tkinter.Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kev514020@gmail.com")
pass_entry = tkinter.Entry(width=33)
pass_entry.grid(row=3, column=1)

gen_button = tkinter.Button(text="Generate Password", command=gen)
gen_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", command=add, width=44)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()