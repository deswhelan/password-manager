from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
LOGO_IMAGE = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=LOGO_IMAGE)
canvas.grid(column=2, row=1)


label_website = Label(text="Website:")
label_website.grid(column=1, row=2, sticky=E)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=1, row=3, sticky=E)

label_password = Label(text="Password:")
label_password.grid(column=1, row=4, sticky=E)

entry_website = Entry(width=45)
entry_website.grid(column=2, row=2, columnspan=2)

entry_email_username = Entry(width=45)
entry_email_username.insert(0, "wheland6@gmail.com")
entry_email_username.grid(column=2, row=3, columnspan=2)

entry_password = Entry(width=35)
entry_password.grid(column=2, row=4)

button_add = Button(width=38, text="Add")
button_add.grid(column=2, row=5, columnspan=2)

button_generate_password = Button(text="Generate")
button_generate_password.grid(column=3, row=4)

window.mainloop()