import json
from json import JSONDecodeError
from password_generator import generate_password
from tkinter import *
from tkinter import messagebox

USER_EMAIL_ADDRESS = "wheland6@gmail.com"

def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            website_name = entry_website.get()

            try:
                website_details = data[website_name]
            except KeyError:
                messagebox.showinfo(title="Not found", message=f"No password found for website \"{website_name}\"")
            else:
                # TODO: stretch - show password in entry_password and copy to clipboard
                messagebox.showinfo(title=website_name, message=f"Email/username: {website_details["email/username"]}\nPassword: {website_details["password"]}")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found!")

def save():
    if form_is_valid():
        website = entry_website.get()
        email_username = entry_email_username.get()
        password = entry_password.get()

        new_data = {
            website: {
                "email/username": email_username,
                "password": password
            }
        }

        is_ok = messagebox.askokcancel(title="Confirm Details", message=f"Save the details below for {website}?\n\nEmail/Username: {email_username}\n\nPassword: {password}")

        if is_ok:
            # TODO: add data file(s) to gitignore
            # TODO: stretch - write to file outside project
            try:
                with open("data.json", mode="r") as data_file:
                    try:
                        # read existing data
                        data = json.load(data_file)
                    # handle empty json file
                    except JSONDecodeError:
                        data = {}
                    finally:
                        # update with new data and write/save
                        with open("data.json", mode="w") as data_file:
                            data.update(new_data)
                            json.dump(data, data_file, indent=4)
            # handle no json file
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            reset_form()

def form_is_valid():
    entry_dict = {
        "website": entry_website.get(),
        "email/username": entry_email_username.get(),
        "password": entry_password.get()
    }

    for entry in entry_dict:
        if len(entry_dict[entry]) < 1:
            messagebox.showwarning(title="Form incomplete", message=f"Please enter {entry}")
            return False

    # TODO: stretch - check for existing entry for a given website before saving
    return True

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

entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(column=2, row=2)

entry_email_username = Entry(width=45)
entry_email_username.insert(0, USER_EMAIL_ADDRESS)
entry_email_username.grid(column=2, row=3, columnspan=2)

entry_password = Entry(width=35)
entry_password.grid(column=2, row=4)

button_search = Button(width=7, text="Search", command=find_password)
button_search.grid(column=3, row=2)

button_generate_password = Button(text="Generate", command= lambda: generate_password(entry_password))
button_generate_password.grid(column=3, row=4)

button_add = Button(width=38, text="Add", command=save)
button_add.grid(column=2, row=5, columnspan=2)

window.mainloop()