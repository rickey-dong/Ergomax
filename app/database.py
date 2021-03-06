import sqlite3

# from flask import Flask

DB_FILE="database.db"

###############
#             #
# Basic Setup #
#             #
###############

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY,
      username TEXT,
      password TEXT
    )""")

# Save and close

db.commit()
db.close()
#####################
#                   #
# Utility Functions #
#                   #
#####################


def fetch_user_id(username, password):
    """
    Gets the id of the user with the given username/password combination from the database.
    Returns None if the combination is incorrect.
    """
    db = sqlite3.connect(DB_FILE)

    # The following line turns the tuple into a single value (sqlite3 commands always return a tuple, even when it is one value)
    # You can read more about row_factory in the official docs:
    # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
    db.row_factory = lambda curr, row: row[0]
    c = db.cursor()

    c.execute("""
        SELECT id
        FROM   users
        WHERE  LOWER(username) = LOWER(?)
        AND    password = ?
    """, (username, password))

    # user_id is None if no matches were found
    user_id = c.fetchone()

    db.close()

    return user_id


def register_user(username, password):
    """
    Tries to add the given username and password into the database.
    Returns False if the user already exists, True if it successfully added the user.
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(?)", (username,))
    row = c.fetchone()

    if row is not None:
        return False

    c.execute("""INSERT INTO users(username,password) VALUES(?, ?)""",(username,password))
    db.commit()
    db.close()
    return True


def fetch_username(user_id):
    """
    Returns the username of the user with the given id.
    """
    db = sqlite3.connect(DB_FILE)
    db.row_factory = lambda curr, row: row[0]
    c = db.cursor()

    c.execute("SELECT username FROM users WHERE id = ?", (user_id,))
    username = c.fetchone()

    db.close()
    return username
