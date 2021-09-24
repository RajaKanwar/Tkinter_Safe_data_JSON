from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import json
import datetime
#  -------------------Password genrator-----------------------
def pass_gen():
    letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z')
    symbol = ('!', '@', '#', '$', '%', '^', '&', '*', '(', '(', ')', '_', '+')
    number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

    password_letter = [choice(letter) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbol) for _ in range(randint(2, 4))]
    password_number = [choice(number) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
#  -------------------Save password----------------------------
def save():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    date = date_entry.get()
    new_data = {
        id: {
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "phone": phone,
            "password": password,
            "Date": date,
        }
    }
    if len(id) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oop", message="please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            age_entry.delete(0, END)
            gender_entry.delete(0, END)
            email_entry.delete(0, END)
            phone_entry.delete(0, END)
            password_entry.delete(0, END)
            date_entry.delete(0, END)
#  -------------------FIND PASSWORD setup---------------------------------
def find_pass():
    id = id_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="NO data data found")
    else:
        if id in data:
            name = data[id]["name"]
            age = data[id]["age"]
            gender = data[id]["gender"]
            phone = data[id]["phone"]
            email = data[id]["email"]
            password = data[id]["password"]
            date = data[id]["Date"]
            messagebox.showinfo(title=id, message=f"Name: {name} Age: {age}\n gender:{gender}\n phone: {phone}\n Email: {email}\nPassword: {password}\n Date: {date}\n")
        else:
            messagebox.showinfo(title=id, message=f"No details for {id} exist.")
# --------------------- Current date ----------------------------
def date():
    current_date = datetime.datetime.now()
    current_date.strftime("%d-%m-%y %H:%M")
    date_entry.insert(0, current_date)


window = Tk()
window.title("Details")
window.geometry("840x630")
window.config(bg="light blue")

frame1 = Frame(window, height=580, width=330, bg="green")
frame1.grid(column=0, row=0)

canvas = Canvas(frame1, height=693, width=350)
l_img = PhotoImage(file="left_img.png")
canvas.create_image(160, 280, image=l_img)
canvas.grid(column=0, row=1)

frame2 = Frame(window, bg="white", height=580, width=330)
frame2.grid(column=1, row=0, ipadx=20)
# Lable
top_lable = Label(frame2, text="SECURE DETAILS", bg="white", font="Impact").grid(column=2, row=0, pady=20, padx=20, columnspan=2)
id_lable = Label(frame2, text="ID", bg="white", font="Candara").grid(column=1, row=1, pady=20, padx=20)
name_lable = Label(frame2, text="Name", bg="white", font="Candara").grid(column=1, row=2, pady=20, padx=20)
age_lable = Label(frame2, text="Age", bg="white", font="Candara").grid(column=3, row=2, pady=20, padx=20)
gender_lable = Label(frame2, text="Gender", bg="white", font="Candara").grid(column=1, row=3, pady=20, padx=20)
email_lable = Label(frame2, text="Email", bg="white", font="Candara").grid(column=1, row=4, pady=20, padx=20)
phone_lable = Label(frame2, text="Phone", bg="white", font="Candara").grid(column=1, row=5, pady=20, padx=20)
password_lable = Label(frame2, text="Password", bg="white", font="Candara").grid(column=1, row=6, pady=20, padx=20)
date_lable = Label(frame2, text="Date", bg="white", font="Candara").grid(column=1, row=7, pady=20, padx=20)

# Entry
id_entry = Entry(frame2, width=15, border=2)
id_entry.grid(column=2, row=1, pady=20, padx=20)
name_entry = Entry(frame2, width=15, border=2)
name_entry.grid(column=2, row=2, pady=20, padx=20)
age_entry = Entry(frame2, width=5, border=2)
age_entry.grid(column=4, row=2, pady=20, padx=20)
gender_entry = Entry(frame2, width=15, border=2)
gender_entry.grid(column=2, row=3, pady=20, padx=20)
email_entry = Entry(frame2, width=15, border=2)
email_entry.grid(column=2, row=4, pady=20, padx=20)
phone_entry = Entry(frame2, width=15, border=2)
phone_entry.grid(column=2, row=5, pady=20, padx=20)
password_entry = Entry(frame2, width=15, border=2)
password_entry.grid(column=2, row=6, pady=20, padx=20)
date_entry = Entry(frame2, width=15, border=2)
date_entry.grid(column=2, row=7, pady=20, padx=20)


# Button
search_button = Button(frame2, text="search", command=find_pass, bg="orange").grid(column=3, row=1, pady=20, padx=20)
genrate_pass_button = Button(frame2, text="Genrate Password", command=pass_gen, bg="orange").grid(column=3, row=6, pady=20, padx=20)
current_date_button = Button(frame2, text="Current date", command=date, bg="orange").grid(column=3, row=7, pady=20, padx=20)
Submite_button = Button(frame2, text="SUBMITE", command=save, bg="orange").grid(column=2, row=11, pady=20, padx=20)

window.mainloop()