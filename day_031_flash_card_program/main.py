import random
from tkinter import *
import pandas

BG_COLOUR="#B1DDC6"


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/worlds_in_German.csv")
    df = pandas.DataFrame(data)
    df.to_csv("data/words_to_learn.csv", index = False)
words_to_learn = data.to_dict(orient="records")
new_word = random.choice(words_to_learn)

def backside():
    global new_word
    card_canvas.itemconfig(background_image, image=card_back_image)
    card_canvas.itemconfig(language_label, fill = "white", text = "English")
    card_canvas.itemconfig(word_label, fill = "white", text =new_word["English"])


def next_card():
    global new_word,timer
    window.after_cancel(timer)
    new_word = random.choice(words_to_learn)
    card_canvas.itemconfig(background_image, image=card_front_image)
    card_canvas.itemconfig(language_label, text= "German", fill = "black")
    card_canvas.itemconfig(word_label, text=new_word["German"], fill ="black")
    timer = window.after(5000, backside)


def right_button_press():
    global words_to_learn
    words_to_learn.remove(new_word)
    wf = pandas.DataFrame(words_to_learn)
    wf.to_csv("data/words_to_learn.csv", index = False)
    next_card()


window = Tk()
window.title("Flash Card Program")
window.config(padx=50,pady=50, bg=BG_COLOUR)

timer = window.after(1000, backside)

# Create card front with labels for texts
card_canvas = Canvas(width=800,height=530)
card_front_image =PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
background_image = card_canvas.create_image(400, 265, image=card_front_image)
card_canvas.config(bg=BG_COLOUR,highlightthickness=0)
language_label = card_canvas.create_text(400, 115, font=("Arial", 40,"italic"))
word_label = card_canvas.create_text(400, 315, font=("Arial", 60, "bold"))
card_canvas.grid(row=0,column=0,columnspan =2)

# Create button for knowing the answer
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(command=right_button_press,image=right_button_image)
right_button.config(bg=BG_COLOUR, highlightthickness=0)
right_button.grid(row=1, column=0)
# sticky="e"
# Create button for not knowing the answer
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=next_card,image=wrong_button_image)
wrong_button.config(bg=BG_COLOUR, highlightthickness=0)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
