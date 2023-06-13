from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "your_secret_key_here"


@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 0
    return render_template("index.html", count=session["count"])


@app.route("/add", methods=["POST"])
def add():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return redirect(url_for("index"))


@app.route("/decrease", methods=["POST"])
def decrease():
    if "count" not in session:
        session["count"] = 0
    session["count"] -= 1
    return redirect(url_for("index"))


@app.route("/destroy_session/", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
