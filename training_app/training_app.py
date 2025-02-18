from datetime import datetime
from tkinter import *
from tkinter import messagebox

COLOR_DARK_BLUE ="RoyalBlue3"
COLOR_LIGHT_BLUE ="sky blue"
PRZEMEK_FOLDER="Przemek_training.txt"
KINGA_FOLDER= "Kinga_training.txt"


def save(data: dict,folder: str):
    try:
        with open(folder, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []
    new_row = f"{data['day']:<10} {data['distance run']:<15} {data['dumbbell shoulder press']:<25} {data['sit-ups']:<10} {data['plank']:<10}\n"
    with open(folder, "a") as file:
        if not lines:
            file.write (f"{'day':<10} {'distance run':<15} {'dumbbell shoulder press':<25} {'sit-ups':<10} {'plank':<10}\n")
        file.write(new_row)


def button_add_p():
    ok= True
    if (day_p_entry.get() == "" or distance_p_entry.get() =="" or dumbbell_p_entry.get() ==""
        or sit_ups_p_entry.get()=="" or plank_p_entry.get() ==""):
        ok = messagebox.askokcancel(title="Przemek",message=f"not all data entered"
                                                                 f"save?")
    if ok:
        new_data = {'day': day_p_entry.get(), 'distance run': distance_p_entry.get(),
                    "dumbbell shoulder press": dumbbell_p_entry.get(),
                    "sit-ups":sit_ups_p_entry.get(),
                    "plank":plank_p_entry.get()}
        save(data=new_data,folder=PRZEMEK_FOLDER)
        day_p_entry.delete(0, END)
        day_p_entry.insert(END, string=f"{datetime.now().strftime("%d.%m")}")
        distance_p_entry.delete(0, END)
        dumbbell_p_entry.delete(0, END)
        sit_ups_p_entry.delete(0, END)
        plank_p_entry.delete(0, END)
        messagebox.showinfo(title="Save data", message="Przemek's data saved")


def button_add_k():
    ok= True
    if (day_k_entry.get() == "" or distance_k_entry.get() =="" or dumbbell_k_entry.get() ==""
        or sit_ups_k_entry.get()=="" or plank_k_entry.get() ==""):
        ok = messagebox.askokcancel(title="Kinga", message=f"not all data entered"
                                                                  f"save?")
    if ok:
        new_data = {'day': day_k_entry.get(), 'distance run': distance_k_entry.get(),
                    "dumbbell shoulder press": dumbbell_k_entry.get(),
                    "sit-ups":sit_ups_k_entry.get(),
                    "plank":plank_k_entry.get()}
        save(data=new_data, folder=KINGA_FOLDER)
        day_k_entry.delete(0, END)
        day_k_entry.insert(END, string=f"{datetime.now().strftime("%d.%m")}")
        distance_k_entry.delete(0, END)
        dumbbell_k_entry.delete(0, END)
        sit_ups_k_entry.delete(0, END)
        plank_k_entry.delete(0, END)
        messagebox.showinfo(title="Save data", message="Kinga's data saved")

def button_add_both():
    button_add_k()
    button_add_p()



window = Tk()
window.title("Training P + K")
window.config(padx=30,pady=30, bg=COLOR_LIGHT_BLUE )

#create logo
canvas = Canvas(width=200,height=200, highlightthickness=0, bg=COLOR_LIGHT_BLUE)
logo_image =PhotoImage(file="logo.png")
canvas.create_image(102,100,image=logo_image)
canvas.grid(column=0,row=0,columnspan = 3)

#create name labels
przemek_label = Label(text="Przemek", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
przemek_label.grid(column=1,row=1)

kinga_label = Label(text="Kinga", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
kinga_label.grid(column=2,row=1)

#create labels and entries for day
day_label = Label(text="day", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
day_label.grid(column=0,row=2, sticky="e")

day_p_entry = Entry()
day_p_entry.insert(END, string=f"{datetime.now().strftime("%d.%m")}")
day_p_entry.grid(column=1,row=2)

day_k_entry = Entry()
day_k_entry.insert(END, string=f"{datetime.now().strftime("%d.%m")}")
day_k_entry.grid(column=2,row=2)

#create labels and entries for distance run
distance_label = Label(text="distance run", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
distance_label.grid(column=0,row=3, sticky="e")

distance_p_entry = Entry()
distance_p_entry.grid(column=1,row=3)

distance_k_entry = Entry()
distance_k_entry.grid(column=2,row=3)

#create labels and entries for dumbbell shoulder press
dumbbell_label = Label(text="dumbbell shoulder press", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
dumbbell_label.grid(column=0,row=4, sticky="e")

dumbbell_p_entry = Entry()
dumbbell_p_entry.grid(column=1,row=4)

dumbbell_k_entry = Entry()
dumbbell_k_entry.grid(column=2,row=4)

#create labels and entries for sit-ups
sit_ups_label = Label(text="sit-ups", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
sit_ups_label.grid(column=0,row=5, sticky="e")

sit_ups_p_entry = Entry()
sit_ups_p_entry.grid(column=1,row=5)

sit_ups_k_entry = Entry()
sit_ups_k_entry.grid(column=2,row=5)

#create labels and entries for plank
plank_label = Label(text="plank", highlightthickness=0, bg=COLOR_LIGHT_BLUE)
plank_label.grid(column=0,row=6, sticky="e")

plank_p_entry = Entry()
plank_p_entry.grid(column=1,row=6)

plank_k_entry = Entry()
plank_k_entry.grid(column=2,row=6)

#create save buttons
add_p_button = Button(text="add", command=button_add_p,width=18,highlightthickness=0, bg=COLOR_DARK_BLUE)
add_p_button.grid(column=1,row=7)

add_k_button = Button(text="add", command=button_add_k,width=18,highlightthickness=0, bg=COLOR_DARK_BLUE)
add_k_button.grid(column=2,row=7,)

add_both_button = Button(text="add", command=button_add_both,width=38,highlightthickness=0, bg=COLOR_DARK_BLUE)
add_both_button.grid(column=1,row=8,columnspan =2)






window.mainloop()
