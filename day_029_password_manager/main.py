from tkinter import *
import pyperclip
from tkinter import messagebox
from password_generator import generate_password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def button_password():
    new_password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)





# ---------------------------- SAVE PASSWORD ------------------------------- #

def button_add():
    if website_entry.get() !="" and username_entry.get() !="" and password_entry.get() != "":
        is_ok=messagebox.askokcancel(title=website_entry.get(),message=f"This are the details:\n"
                                                                 f"username: {username_entry.get()}\n"
                                                                 f"password: {password_entry.get()}\n"
                                                                 f"save?")
        if is_ok:
            new_data = {'website': website_entry.get(), 'Emile/Username': username_entry.get(),
                        "password": password_entry.get(),
                        }
            try:
                with open("password_list.txt", "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            new_row = f"{new_data['website']:<20} {new_data['Emile/Username']:<30} {new_data['password']:<20}\n"

            with open("password_list.txt", "a") as file:
                if not lines:
                    file.write(f"{'Website':<20} {'Emile/Username':<30} {'Password':<20}\n")
                file.write(new_row)
            pyperclip.copy(password_entry.get())
            password_entry.delete(0, END)
            website_entry.delete(0,END)
            messagebox.showinfo(title="Saved",message="Data saved, password copied into clipboard")
    else:
        messagebox.showinfo(title="Error", message="Check if you entered all the data")


# ---------------------------- UI SETUP ------------------------------- #

# Prepare window
window = Tk()
window.title("Password manager")
# window.minsize(width=200,height=200)
window.config(padx=30,pady=30)

# create Website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0,row=1, sticky="e")

website_entry = Entry(width=44)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan =2,sticky="w")
# print(entry.get())


# create Emile/Username label and entry
username_label = Label(text="Emile/Username:")
username_label.grid(column=0,row=2, sticky="e")

username_entry = Entry(width=44)
username_entry.insert(END, string="@gmail.com")
username_entry.grid(column=1,row=2,columnspan =2,sticky="w")
# print(entry.get())
# entry.pack()

# create password label, entry and button
password_label = Label(text="Password:")
password_label.grid(column=0,row=3, sticky="e")

password_entry = Entry(width=33)
password_entry.grid(column=1,row=3,sticky="w")

password_button = Button(text="generate", command=button_password,)
password_button.grid(column=2,row=3,sticky="e")

# create add button
add_button = Button(text="add", command=button_add,width=37)
add_button.grid(column=1,row=4,columnspan =2,sticky="w")

# create graphics
canvas = Canvas(width=200,height=200)
logo_image =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)











window.mainloop()
