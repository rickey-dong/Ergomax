from flask import Flask, request, redirect, render_template, session
import database

app = Flask(__name__)

def is_logged_in():
    return "user" in session


@app.route("/")
def home():
    if is_logged_in():
        return render_template(
            "home.html",
            user=session["user"],
        )
    return render_template('home.html')


@app.route("/logout")
def logout():
    print("logout page...redirecting to homepage")
    if is_logged_in():
        session.pop("user")
        session.pop("user_id")

    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    if is_logged_in():
        return redirect("/")

    # Default page
    if request.method == 'GET':
        return render_template("login.html")

    # Check login
    username = request.form["username"]
    pas = request.form["password"]

    if username.strip() == "" or pas.strip == "":
        return render_template('login.html', explain="please enter characters and/or numbers")

    # verify this user and password exists
    user_id = database.fetch_user_id(username, pas)
    if user_id is None:
        return render_template('login.html', explain="login information is wrong")

    # Adds user and user id to session
    session["user"] = database.fetch_username(user_id) # Ensures the displayed username is correct casing
    session["user_id"] = user_id
    return redirect("/")

    #except:
    #   return render_template('login.html', explain=
    # "seems like something went wrong! check your username and password combination! you may also make a new account")


@app.route("/register", methods=["GET", "POST"])
def register():
    if is_logged_in():
        return redirect("/")

    # Default page
    if request.method == "GET":
        return render_template('register.html')

    # Check login
    user = request.form["newusername"]
    pwd = request.form["newpassword"]
    if user.strip() == "" or pwd.strip == "":
        return render_template('register.html', explain="please enter characters and/or numbers")

    register_success = database.register_user(user, pwd)
    if not register_success:
        return render_template('register.html', explain="username already exists")

    return redirect("/login")

@app.route("/about", methods=['GET', 'POST'])
def about():
    if is_logged_in():
        return render_template("about.html")
    return render_template("about.html", user=session['name'])

@app.route("/example", methods=['GET', 'POST'])
def example():
    if is_logged_in():
        return render_template("example.html")
    return render_template("example.html", user=session['name'])

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "It's Rewind Time"
    app.run()
