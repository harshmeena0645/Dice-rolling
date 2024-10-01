from tkinter import *
import random

root = Tk()
root.geometry("700x600")
root.title("Roll Dice")

label = Label(root, text="", font=("times", 260))

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice_color = random.choice(['#FF6347', '#6A5ACD', '#32CD32', '#FFD700', '#00BFFF', '#FF4500'])
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}', fg=dice_color)
    label.pack()

def on_enter(e):
    button['background'] = '#FF4500'

def on_leave(e):
    button['background'] = '#4CAF50'

button = Button(root, text="Let's Roll", width=40, height=5, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", bd=2, command=roll)
button.pack(padx=10, pady=10)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
root.configure(bg="#ADD8E6")

root.mainloop()

#harshmeena0645