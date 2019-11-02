from flask import Flask, render_template
import string_generator as sg

g = sg.generator()

app = Flask(__name__)

@app.route('/')
def index():
    string = g.generate_string(5)
    print(string)
    return render_template("index.html", string=string)