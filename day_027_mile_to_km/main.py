from tkinter import *


def button_click():
    value = int(entry.get())
    value = round(value * 1.60934,0)
    calculate_label.config(text=value)


window = Tk()
window.title("Kilometer to miles")
window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

# Entry
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1,row=0)


miles_label = Label(text="Miles", font=("Arial", 16,""))
miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to: ", font=("Arial", 16, ""))
equal_label.grid(column=0,row=1)

calculate_label = Label(text="0", font=("Arial", 16, ""))
calculate_label.grid(column=1,row=1)

kilometers_label = Label(text="Kilometers", font=("Arial", 16, ""))
kilometers_label.grid(column=2, row=1)

button = Button(text="calculate", command=button_click)
button.grid(column=1,row=2)
button.config(padx=10,pady=10)








window.mainloop()