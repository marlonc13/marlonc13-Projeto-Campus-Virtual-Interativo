from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template("inicial.html")

@app.route("/")
def inicial():
    return render_template("instalações.html")

@app.route("/")
def inicial():
    return render_template("Clubes.html")

@app.route("/")
def inicial():
    return render_template("SUporte.html")

@app.route("/")
def inicial():
    return render_template("Trasporte.html")

