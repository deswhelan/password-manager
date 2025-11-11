from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
LOGO_IMAGE = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=LOGO_IMAGE, anchor="c")
canvas.grid(column=2, row=2)

window.mainloop()