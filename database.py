import sqlite3
import hashlib
import hmac
import secrets


# Connect to the database
def get_connection():
    connection = sqlite3.connect("password_manager.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

# Create database and tables
def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)
    # Accounts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            website TEXT NOT NULL,
            account_username TEXT NOT NULL,
            password TEXT NOT NULL,

            FOREIGN KEY (user_id)
            REFERENCES users(user_id)
            ON DELETE CASCADE
        )
    """)

    connection.commit()
    connection.close()

# Register a new user
def register_user(username, password):
    salt = secrets.token_hex(16)

    # Hash the master password
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        bytes.fromhex(salt),
        200000
    ).hex()
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (username, password_hash, salt)
            VALUES (?, ?, ?)
        """, (username, password_hash, salt))

        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()

# Verify user login
def verify_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Find the user
        cursor.execute("""
            SELECT user_id, password_hash, salt
            FROM users
            WHERE username = ?
        """, (username,))

        user = cursor.fetchone()

    finally:
        connection.close()

    # Username doesn't exist
    if user is None:
        return None
    # Extract database values
    user_id = user[0]
    stored_hash = user[1]
    salt = user[2]

    # Hash the entered password
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        bytes.fromhex(salt),
        200000
    ).hex()

    # Compare password hashes
    if hmac.compare_digest(password_hash, stored_hash):
        return user_id

    return None


# Add a website account
def add_account(user_id, website, account_username, password):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO accounts (
                user_id,
                website,
                account_username,
                password
            )
            VALUES (?, ?, ?, ?)
        """, (user_id, website, account_username, password))

        connection.commit()
        return True
    except sqlite3.Error:
        return False

    finally:
        connection.close()

# Retrieve accounts belonging to a specific user
def get_accounts(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT account_id, website, account_username, password
            FROM accounts
            WHERE user_id = ?
        """, (user_id,))

        accounts = cursor.fetchall()

        return accounts
    finally:
        connection.close()


# Run database creation when this file is executed directly
if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
