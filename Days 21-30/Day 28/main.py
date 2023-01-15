from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Background and tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 150, text="00:00", fill="white", font=(FONT_NAME, 35,
                                                               "bold"))
canvas.grid(column=1, row=1)

# Timer label
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"),
              highlightthickness=0, bg=YELLOW)
label.grid(column=1, row=0)

# Start button
button = Button(text="Start")
button.grid(column=0, row=2)

# Reset button
button = Button(text="Reset")
button.grid(column=2, row=2)

# Checkmark label
label = Label(text="✔", fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0, bg=YELLOW)
label.grid(column=1, row=3)


window.mainloop()

