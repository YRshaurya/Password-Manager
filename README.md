# 🔐 Password Manager

A desktop-based Password Manager built using Python, Tkinter and SQLite. This project allows users to register, log in and securely manage their website credentials through a simple graphical user interface.

The project is currently under development and is open to improvements, new features and contributions.

## ✨ Features Implemented

- **User Registration:** Create a new account with a unique username and password.
- **User Login:** Authenticate users using their registered credentials.
- **Password Hashing:** Master passwords are hashed using PBKDF2-HMAC with SHA-256 and individual salts.
- **SQLite Database:** Store user information and website credentials locally.
- **Add Website Accounts:** Save website names, account usernames and passwords.
- **View Saved Accounts:** Retrieve and display saved website credentials.
- **User-Specific Data:** Each user can access only their own saved website accounts.
- **GUI Interface:** Desktop interface built using Tkinter.
- **Database Relationships:** Foreign key relationships with cascading deletion support.

## 🛠️ Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Core programming language     |
| Tkinter    | Graphical User Interface      |
| SQLite     | Local database                |
| hashlib    | Password hashing              |
| hmac       | Secure hash comparison        |
| secrets    | Cryptographic salt generation |

## 📁 Project Structure

```text
Password Manager/
│
├── main.py              # Application entry point and login/registration
├── dashboard.py         # Main dashboard interface
├── account_pages.py     # Add and view website accounts
├── database.py          # Database operations and authentication
│
├── password_manager.db  # Local SQLite database (generated locally)
├── requirements.txt     # Python dependencies
├── .gitignore           # Files excluded from Git
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd "Password Manager"
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

For macOS/Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Run the application

```bash
python3 main.py
```

**Note:** Python must have Tkinter support installed. On some macOS installations, a separate Tk-compatible Python installation may be required.

## 🔒 Security Notes

- Master account passwords are hashed using PBKDF2-HMAC with SHA-256 and individual random salts.
- Website credentials are currently stored in plaintext in the local SQLite database.
- Database access is local to the application.
- Encryption for stored website passwords has not yet been implemented.

This is currently a learning project and should not be used to store real or sensitive credentials until additional security measures are implemented.

## 🛣️ Future Improvements

The project is open for improvement. Some planned features include:

- [ ] Delete user accounts.
- [ ] Delete individual saved website credentials.
- [ ] Edit saved website names, usernames and passwords.
- [ ] Implement encryption for stored website passwords.
- [ ] Add a password generator with customizable options.
- [ ] Add a search feature to find saved website credentials.
- [ ] Add a copy-to-clipboard option for usernames and passwords.
- [ ] Add a show/hide password toggle.
- [ ] Improve the overall GUI design and user experience.
- [ ] Add password strength checking.
- [ ] Package the application into a standalone desktop executable.

## 🤝 Contributions

This project is open to contributions and improvements.

If you have ideas for new features, bug fixes or improvements, feel free to fork the repository, make your changes and submit a pull request.

Suggestions and constructive feedback are always welcome!

## 📌 Project Status

**Status:** Under Development 🚧

This project is being developed as a hands-on learning experience to understand Python, GUI development, database management, authentication and application architecture.

More features and improvements will be added over time.

---

Made with Python 🐍
