def add(*args):
    sum = 0
    for number in args:
        sum += number
    print (sum)


# add(2,3,5,8,8)
def calculate(n,**kwargs):
    n *= kwargs.get("multiply")
    n += kwargs.get("add")
    print(n)

calculate(5,add = 3, multiply= 2)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

    def car_print(self):
        print(f"make: {self.make}, model: {self.model}")

car = Car(make="Volkswagen")
car.car_print()





from tkinter import *

def button_click():
    value = entry.get()
    my_label.config(text=value)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

# Label
my_label = Label(text="I am label", font=("Arial", 16,""))
my_label.grid(column=0,row=0)
my_label.config(padx=10,pady=10)

# Button
button = Button(text="button1", command=button_click)
button.grid(column=1,row=1)
button.config(padx=10,pady=10)

new_button = Button(text="button2", command=button_click)
new_button.grid(column=2,row=0)
new_button.config(padx=10,pady=10)
# Entry
entry = Entry(width=10)
entry.grid(column=3,row=2,padx=10,pady=10)



window.mainloop()