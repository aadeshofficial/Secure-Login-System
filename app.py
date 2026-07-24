from flask import Flask, render_template, request, redirect, session, url_for
from auth import register_user, login_user

# Create Flask application
app = Flask(__name__)

# Secret key used for session management
app.secret_key = "my_secret_key"

# Home Page
@app.route("/")
def home():
    # Check if user is logged in
    if "username" in session:
        return f"""<h2>Welcome, {session['username']}!</h2>
        <br>
        <a href='/logout'>Logout</a>
        """

    # Redirect to login page if not logged in
    return redirect("/login")


# User Registration
@app.route("/register", methods=["GET", "POST"])
def register():

    # Process registration form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Register new user
        if register_user(username, password):
            return redirect("/login")
        else:
            return "Username already exists!"

    # Registration form
    return """
    <h2>Register</h2>
    <form method="POST">
        Username:<br>
        <input type="text" name="username" required><br><br>

        Password:<br>
        <input type="password" name="password" required><br><br>

        <input type="submit" value="Register">
    </form>

    <br>
    <a href="/login">Already have an account? Login</a>
    """


# User Login
@app.route("/login", methods = ["GET", "POST"])
def login():

    # Process login form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Verify user credentials
        if login_user(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return "Invalid Username or Password!"

    # Login form
    return"""
    <h2>Login</h2>
    <form method = "POST">
    Username:<br>
    <input type = "text" name = "username" required><br><br>
    
    Password:<br>
    <input type = "password" name = "password" required><br><br>
    
    <input type = "submit" value = "Login"></form>
    
    <br>
    <a href = "/register">Create a New Account</a>
    """

# Logout user and clear session
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

# Start the Flask development server
if __name__ == "__main__":
    app.run(debug = True)