
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math
import pygame
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25*60
SHORT_BREAK_SEC = 5*60
LONG_BREAK_SEC = 20*60
CHECK_MARK= "✔"
reps = 0
check_marks= ""
timer = None


pygame.mixer.init()
pygame.mixer.music.load("gong.mp3")

# ---------------------------- TIMER RESET ------------------------------- #

def button_reset():
    global reps
    global check_marks
    global timer
    reps = 0
    check_marks =""
    check_marks_label.config(text=check_marks)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    pass

# def increase_check_marks():
#     new_text =
#     check_marks.config(text="✔")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def button_start():
    global reps
    global check_marks
    if reps == 9:
        label.config(text="Break",fg=RED)
        count_down(LONG_BREAK_SEC)
        button_reset()
    elif reps%2 == 1 and reps < 8:
        label.config(text="Break",fg=PINK)
        count_down(SHORT_BREAK_SEC)
    else:
        label.config(text="Work")
        count_down(WORK_SEC)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    global check_marks
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds in range(0,10):
        seconds ="0"+str(seconds)
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count-1)
    else:
        pygame.mixer.music.play()
        if reps == 9:
            button_reset()
        if reps%2 ==0:
            check_marks += CHECK_MARK
            check_marks_label.config(text=check_marks)
        reps += 1
        button_start()

# ---------------------------- UI SETUP ------------------------------- #
# Prepare window
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)
# create title
label = Label(text="Timer")
label.config(bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
label.grid(column=1,row=0)

#create tick mark
check_marks_label = Label()
check_marks_label.config(bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
check_marks_label.grid(column=1,row=4)


# create tomato and timer graphics
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_image =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#creates start buttons
start_button = Button(text="start", command=button_start,font=(FONT_NAME,10),highlightthickness=0)
start_button.grid(column=0,row=2)
start_button.config(padx=10,pady=10)

resset_button = Button(text="reset", command=button_reset,font=(FONT_NAME,10),highlightthickness=0)
resset_button.grid(column=3,row=2)
resset_button.config(padx=10,pady=10)






window.mainloop()



