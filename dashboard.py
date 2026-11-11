import tkinter as tk
from account_pages import show_add_account, show_view_accounts

def show_dashboard(root, go_back, user_id):

    dashboard = tk.Frame(root, bg="#c8c8c8")

    # Header container
    screenTwo = tk.Frame(dashboard, bg="#c8c8c8")
    screenTwo.pack(fill="both", expand=True)

    header = tk.Frame(
        screenTwo,
        bg="#1769AA",
        height=40
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    welcome = tk.Label(
        header,
        text="Welcome to your Dashboard",
        font=("Segoe UI", 12),
        bg="#1769AA",
        fg="white"
    )
    welcome.pack(side="left", padx=15)

    # Left sidebar
    leftSidebar = tk.Frame(
        screenTwo,
        bg="white",
        width=200,
        height=380,
        bd=1,
        relief="solid"
    )

    leftSidebar.pack(
        side="left",
        fill="y",
        padx=(20, 5),
        pady=(20, 25)
    )

    leftSidebar.pack_propagate(False)

    # Right sidebar (hidden)
    rightSidebar = tk.Frame(
        screenTwo,
        bg="white",
        bd=1,
        relief="solid"
    )

    # Scrollable Canvas
    canvas = tk.Canvas(
        rightSidebar,
        bg="white",
        highlightthickness=0
    )

    # Scrollbar
    scrollbar = tk.Scrollbar(
        rightSidebar,
        orient="vertical",
        command=canvas.yview
    )

    # Main content inside Canvas
    mainContent = tk.Frame(
        canvas,
        bg="white"
    )

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas_window = canvas.create_window(
        (0, 0),
        window=mainContent,
        anchor="nw"
    )

    # Update scrolling region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    mainContent.bind("<Configure>", update_scroll_region)

    # Adjust content width
    def resize_content(event):
        canvas.itemconfigure(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_content)

    # Display Canvas and scrollbar
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Show right sidebar
    def show_right_sidebar():
        if not rightSidebar.winfo_ismapped():
            rightSidebar.pack(
                side="right",
                fill="both",
                expand=True,
                padx=(10, 15),
                pady=(20, 5)
            )

    # Add Account button
    add_account_btn = tk.Button(
        leftSidebar,
        text="Add Account",
        font=("Segoe UI", 12),
        width=15,
        bg="white",
        bd=1,
        relief="solid",
        highlightthickness=0,
        command=lambda: (
            show_right_sidebar(),
            show_add_account(mainContent, user_id)
        )
    )
    add_account_btn.pack(fill="x", padx=10, pady=5)

    # View Accounts button
    view_accounts_btn = tk.Button(
        leftSidebar,
        text="View Accounts",
        font=("Segoe UI", 12),
        width=15,
        bg="white",
        bd=1,
        relief="solid",
        highlightthickness=0,
        command=lambda: (
            show_right_sidebar(),
            show_view_accounts(mainContent, user_id)
        )
    )
    view_accounts_btn.pack(fill="x", padx=10, pady=5)

    # Bottom buttons
    button_frame = tk.Frame(screenTwo, bg="#c8c8c8")
    button_frame.pack(
        side="bottom",
        anchor="e",
        padx=25,
        pady=(20, 25)
    )

    exit_btn = tk.Button(
        button_frame,
        text="Exit",
        font=("Segoe UI", 12),
        width=5,
        bd=1,
        relief="solid",
        highlightthickness=0, 
        command=root.destroy,
        padx= 2,
        highlightbackground="#dddddd"
    )
    exit_btn.pack(side="left")

    prev_btn = tk.Button(
        button_frame,
        text="Prev",
        font=("Segoe UI", 12),
        width=5,
        bd=1,
        bg="white",
        relief="solid",
        highlightthickness=0, 
        padx= 2,
        highlightbackground="#dddddd",
        command= go_back,
    )
    prev_btn.pack(side="left")

    return dashboard