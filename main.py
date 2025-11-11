from tkinter import *

USER_EMAIL_ADDRESS = "wheland6@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # TODO: stretch - check for values before saving
    # TODO: stretch - check for existing entry for a given website before saving
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    # TODO: stretch - write to file outside project
    with open("data.txt", mode="a") as data_file:
        data_file.write(f"{website} | {email_username} | {password}\n")

    reset_form()

def reset_form():
    entry_website.delete(0, "end")
    entry_email_username.delete(0, "end")
    entry_password.delete(0, "end")
    entry_email_username.insert(0, USER_EMAIL_ADDRESS)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
LOGO_IMAGE = PhotoImage(file="logo.png")
canvas.create_image(85, 100, image=LOGO_IMAGE)
canvas.grid(column=2, row=1)

label_website = Label(text="Website:")
label_website.grid(column=1, row=2, sticky=E)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=1, row=3, sticky=E)

label_password = Label(text="Password:")
label_password.grid(column=1, row=4, sticky=E)

entry_website = Entry(width=45)
entry_website.focus()
entry_website.grid(column=2, row=2, columnspan=2)

entry_email_username = Entry(width=45)
entry_email_username.insert(0, USER_EMAIL_ADDRESS)
entry_email_username.grid(column=2, row=3, columnspan=2)

entry_password = Entry(width=35)
entry_password.grid(column=2, row=4)

button_add = Button(width=38, text="Add", command=save)
button_add.grid(column=2, row=5, columnspan=2)

button_generate_password = Button(text="Generate")
button_generate_password.grid(column=3, row=4)

window.mainloop()