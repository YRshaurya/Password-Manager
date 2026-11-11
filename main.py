import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from dashboard import show_dashboard
from database import create_database, register_user, verify_user

create_database()

root = tk.Tk()
root.title("Password Manager")
root.geometry("550x550")
root.configure(bg="#fbfbfb")
style = ttk.Style()
style.theme_use("classic")

# Main screen
screenOne = tk.Frame(root, bg="#c8c8c8")
screenOne.pack(fill="both", expand=True)

# Header container
header = tk.Frame(
    screenOne,
    bg="#1769AA",
    height=40
)
header.pack(fill="x")
header.pack_propagate(False)

# Welcome heading
welcome = tk.Label(
    header,
    text="Welcome",
    font=("Segoe UI", 12),
    bg="#1769AA",
    fg="white"
)
welcome.pack(side="left", padx=15)


heading = tk.Label(
    screenOne,
    text="Anything not saved will be lost. \n Type a user name and password to log in",
    bg="#c8c8c8",
    fg="black",
    font=("Segoe UI", 12)
)
heading.pack(side="top", pady=5, padx=10)

# Login form
form = tk.Frame(
    screenOne,
    bg="white",
    bd=1,
    relief="solid"
)
form.pack(
    padx=35,
    pady=15,
    fill="both",
    expand=True
)

# Username label
username_label = tk.Label(
    form,
    text="User name:",
    font=("Segoe UI", 12),
    bg="white",
    fg="black",
)
username_label.grid(row=0, column=0, padx=10, pady=20)

# Username input
username_entry = tk.Entry(
    form,
    font=("Segoe UI", 12),
    width=30,
    bg="white",
    fg="black",
    bd=1,
    relief="solid",
    highlightthickness=0, 
        insertbackground="black"

)
username_entry.grid(row=0, column=1, padx=10, pady=20)

# Username label
password_label = tk.Label(
    form,
    text="Password:",
    font=("Segoe UI", 12),
    bg="white",
    fg="black",
)
password_label.grid(row=1, column=0, padx=10, pady=5)

# Password input
password_entry = tk.Entry(
    form,
    font=("Segoe UI", 12),
    width=30,
    bg="white",
    fg="black",
    bd=1,
    relief="solid",
    highlightthickness=0,
        insertbackground="black",
        show="*"

)
password_entry.grid(row=1, column=1, padx=10, pady=5)

new_user_var = tk.BooleanVar()

new_user_checkbox = tk.Checkbutton(
    form,
    text="New User",
    variable=new_user_var,
    font=("Segoe UI", 12),
    bg="white",
    fg="black",
)
new_user_checkbox.grid(row=2, column=0, padx=10, pady=5)

dashboard = None
def login():
    global dashboard
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning(
            "Missing Details",
            "Please enter username and password."
        )
        return
    # Registration mode
    if new_user_var.get():
        if register_user(username, password):
            messagebox.showinfo(
                "Registration Successful",
                "Your account has been created!"
            )

            new_user_var.set(False)
            username_entry.delete(0, tk.END) # Clear input 
            password_entry.delete(0, tk.END) # Clear input
        else:
            messagebox.showerror(
                "Registration Failed",
                "Username already exists."
            )
    # Login mode
    else:
        user_id = verify_user(username, password)
        if user_id is not None:
            screenOne.pack_forget()

            dashboard = show_dashboard(root, show_login, user_id)
            dashboard.pack(fill="both", expand=True)
        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

def show_login():
    global dashboard
    username_entry.delete(0, tk.END) # Clear input 
    password_entry.delete(0, tk.END)
    if dashboard is not None:
        dashboard.destroy()
        dashboard = None
    screenOne.pack(fill="both", expand=True)


button_frame = tk.Frame(screenOne, bg="white")
button_frame.pack(side="bottom", anchor="e", padx=25, pady=20)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    font=("Segoe UI", 12),
    width=5,
    bd=1,
    relief="solid",
    command=root.destroy,highlightthickness=0,
        highlightbackground="#dddddd"
)

prev_btn = tk.Button(
    button_frame,
    text="Prev",
    font=("Segoe UI", 12),
    width=5,
    bd=1,
    bg="white",
    fg="#8D8C8C",
    relief="solid",
    highlightthickness=0,
    highlightbackground="#dddddd"
)

next_btn = tk.Button(
    button_frame,
    text="Next",
    font=("Segoe UI", 12),
    width=5,
    bd=1,
    relief="solid",
    highlightthickness=0,
    highlightbackground="#dddddd",
    command= login,
)

exit_btn.pack(side="left")
prev_btn.pack(side="left")
next_btn.pack(side="left")

# Keep input column expandable
form.grid_columnconfigure(1, weight=1)

# Run application
root.mainloop()
