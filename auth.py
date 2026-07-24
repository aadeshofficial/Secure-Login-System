import sqlite3
import bcrypt

# Register User
def register_user(username, password):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
        )

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.IntegrityError:
        conn.close()
        return False

# ADD THIS ENTIRE FUNCTION BELOW register_user()
def login_user(username, password):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users  WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            user[0]
        )
    
    return False