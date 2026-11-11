import tkinter as tk
from tkinter import messagebox
from database import add_account, get_accounts

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

def show_add_account(content, user_id):

    clear_content(content)

    heading = tk.Label(
        content,
        text="Add New Account",
        font=("Segoe UI", 12),
        bg="white",
        fg="black"
    )
    heading.pack(pady=10)

    # Website / Application
    website_label = tk.Label(
        content,
        text="Website:",
        fg="black",
        font=("Segoe UI", 12),
        bg="white"
    )
    website_label.pack(pady=5)

    website_entry = tk.Entry(
        content,
        font=("Segoe UI", 12),
        fg="black",
        bg="white",
        bd=1,
        relief="solid",
        highlightthickness=0,
        insertbackground="black"
    )
    website_entry.pack(pady=5)

    # Username
    username_label = tk.Label(
        content,
        text="Username:",
        font=("Segoe UI", 12),
        bg="white",
        fg="black"
    )
    username_label.pack(pady=5)

    username_entry = tk.Entry(
        content,
        font=("Segoe UI", 12),
        bg="white",
        fg="black",
        bd=1,
        relief="solid",
        highlightthickness=0,
        insertbackground="black"
    )
    username_entry.pack(pady=5)

    # Password
    password_label = tk.Label(
        content,
        text="Password:",
        font=("Segoe UI", 12),
        bg="white",
        fg="black"
    )
    password_label.pack(pady=5)

    password_entry = tk.Entry(
        content,
        font=("Segoe UI", 12),
        bg="white",
        fg="black",
        show="*",
        bd=1,
        relief="solid",
        highlightthickness=0,
        insertbackground="black"
    )
    password_entry.pack(pady=5)

    # Save account
    def save_account():

        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        if not website or not username or not password:
            messagebox.showwarning(
                "Missing Details",
                "Please fill in all fields."
            )
            return

        success = add_account(
            user_id,
            website,
            username,
            password
        )

        if success:
            messagebox.showinfo(
                "Success",
                "Account added successfully!"
            )

            show_add_account(content, user_id)

        else:
            messagebox.showerror(
                "Error",
                "Could not save account."
            )

    save_button = tk.Button(
        content,
        text="Save Account",
        font=("Segoe UI", 12),
        bd=1,
        relief="solid",
        highlightthickness=0,
        command=save_account
    )
    save_button.pack(pady=20)


def show_view_accounts(content, user_id):

    clear_content(content)

    heading = tk.Label(
        content,
        text="Saved Accounts",
        font=("Segoe UI", 12),
        bg="white",
        fg="black"
    )
    heading.pack(pady=25)

    # Retrieve accounts from SQLite
    accounts = get_accounts(user_id)
    if not accounts:
        tk.Label(
            content,
            text="No accounts saved yet.",
            font=("Segoe UI", 12),
            bg="white",
            fg="black"
        ).pack(pady=10)
        return

    # Display saved accounts
    for account in accounts:

        account_label = tk.Label(
            content,
            text=(
                f"Website: {account[1]}\n"
                f"Username: {account[2]}\n"
                f"Password: {account[3]}"
            ),
            font=("Segoe UI", 12),
            bg="#fbfbfb",
            width=40,
            fg="black",
            bd=1,
            relief="solid",
            highlightthickness=0
        )

        account_label.pack(pady=5, padx=20)
