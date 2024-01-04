import tkinter as tk
from tkinter import ttk
import mysql.connector

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_registration"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

def register_guest():
    guest_name = name_var.get()
    room_type = room_var.get()
    num_days = int(days_entry.get())
    
    prices = {
        "Single": 100,
        "Double": 200,
        "Suite": 300,
    }
    
    total_price = prices.get(room_type, 0) * num_days
    
    try:
        sql = "INSERT INTO `guests` (Guest_Name, Room_Type, Number_Days, Total_Price) VALUES (%s, %s, %s, %s)"
        val = (guest_name, room_type, num_days, total_price)
        mycursor.execute(sql, val)
        mydb.commit()
        output_label.config(text=f"Guest: {guest_name}, Room: {room_type}, Days: {num_days}, Total Price: RM{total_price}")
        show_success_animation()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        show_error_animation()

def show_success_animation():
    output_label.config(fg="green")
    output_label.after(2000, reset_label)

def show_error_animation():
    output_label.config(fg="red")
    output_label.after(2000, reset_label)

def reset_label():
    output_label.config(text="", fg="margenta")

root = tk.Tk()
root.title("Welcome To Our Hotel Registration!")
root.geometry('500x600')
root.configure(bg='pink')

mydb = connect_to_database()
mycursor = mydb.cursor()

# Page Title
label = tk.Label(root, text='Welcome to Our Hotel', font=("Berlin Sans FB Demi", 18, "bold"), bg='pink', fg='purple')
label.pack(ipadx=10, ipady=10)

# Room Type Dropdown with ttk theme
style = ttk.Style()
style.theme_use('clam')
room_label = tk.Label(root, text="Choose Your Room Type", bg='pink', fg='purple')
room_label.pack()

room_var = tk.StringVar(root)
room_var.set("Select Your Room")  # Default value
room_dropdown = ttk.Combobox(root, textvariable=room_var, values=["Single", "Double", "Suite"], state='readonly')
room_dropdown.pack(pady=10)

# Guest Name Entry
name_label = tk.Label(root, text="Guest Name:", bg='pink', fg='purple')
name_label.pack()
name_var = tk.StringVar(root)
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()

# Number of Days Entry
days_label = tk.Label(root, text="Number of Days:", bg='pink', fg='purple')
days_label.pack()
days_entry = tk.Entry(root)
days_entry.pack()

# Register Button with hover effect
register_button = tk.Button(root, text="Register", command=register_guest, relief=tk.GROOVE, bg='purple', fg='white')
register_button.pack(pady=10)
register_button.bind("<Enter>", lambda event: register_button.config(bg='gold'))
register_button.bind("<Leave>", lambda event: register_button.config(bg='orange'))

# Output Label
output_label = tk.Label(root, text="", font=("Times New Roman", 12), bg='lightblue')
output_label.pack()

root.mainloop()
