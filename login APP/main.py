from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

# Secret key for session
app.secret_key = "my_secret_key"


# =========================
# MySQL Database Connection
# =========================

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="login_system"
    )


# =========================
# Login Page
# =========================

@app.route("/", methods=["GET", "POST"])
@app.route("/login.html", methods=["GET", "POST"])
def login():

    msg = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db_connection()
        cursor = db.cursor()

        query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
        """

        cursor.execute(query, (username, password))

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            session["username"] = username
            return redirect(url_for("login.html"))

        else:
            msg = "Invalid username or password"

    return render_template("login.html", msg=msg)


# =========================
# Registration Page
# =========================

@app.route("registration.html", methods=["GET", "POST"])
def registration():

    msg = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        db = get_db_connection()
        cursor = db.cursor()

        # Check whether username already exists
        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            msg = "Username already exists"

        else:

            query = """
            INSERT INTO users (username, password, email)
            VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (username, password, email)
            )

            db.commit()

            cursor.close()
            db.close()

            return redirect(url_for("login.html"))

        cursor.close()
        db.close()

    return render_template("registration.html", msg=msg)


# =========================
# Welcome Page
# =========================

@app.route("/index")
def index():

    if "username" not in session:
        return redirect(url_for("login.html"))

    name = session["username"]

    return render_template(
        "login.html",
        name=name,
        msg="Login successful"
    )


# =========================
# Logout
# =========================

@app.route("Welcome.html")
def logout():

    session.clear()

    return redirect(url_for("login.html"))


# =========================
# Run Application
# =========================

if __name__ == "__main__":
    app.run(debug=True)