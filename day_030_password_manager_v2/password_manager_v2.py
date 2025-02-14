from json import JSONDecodeError
from tkinter import *
import json
import pyperclip
from tkinter import messagebox
from password_generator import generate_password



def button_password():
    new_password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)

def button_find():
    try:
        with open("password_list.json", "r") as data_file:
            data = json.load(data_file)
    except (JSONDecodeError, FileNotFoundError):
        messagebox.showinfo(title="No account", message="No account found")
    else:
        website = website_entry.get().title()
        if website in data:
            emile = data[website]["Emile"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Emile: {emile}\npassword: {password}")
        else:
            messagebox.showinfo(title="No account", message="No account found")


def button_add():
    website = website_entry.get().title()
    emile = emile_entry.get()
    password = password_entry.get()

    if website !="" and emile != "" and password != "":

        new_data = {
            website:{
            'Emile': emile,
            "password": password}
                    }
        try:
            with open("password_list.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except (JSONDecodeError, FileNotFoundError):
            data = new_data
        finally:
            with open("password_list.json", "w") as data_file:
                json.dump(data,data_file, indent= 4)

            pyperclip.copy(password_entry.get())
            password_entry.delete(0, END)
            website_entry.delete(0,END)
            messagebox.showinfo(title="Saved",message="Data saved, password copied into clipboard")
    else:
        messagebox.showinfo(title="Error", message="Check if you entered all the data")




# Prepare window
window = Tk()
window.title("Password manager")
# window.minsize(width=200,height=200)
window.config(padx=30,pady=30)

# create Website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0,row=1, sticky="e")

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan =2,sticky="w")

website_button = Button(text="find", command=button_find,width=7)
website_button.grid(column=2,row=1,columnspan =2,sticky="e")


# create Emile/Username label and entry
username_label = Label(text="Emile/Username:")
username_label.grid(column=0,row=2, sticky="e")

emile_entry = Entry(width=44)
emile_entry.insert(END, string="@gmail.com")
emile_entry.grid(column=1, row=2, columnspan =2, sticky="w")
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
