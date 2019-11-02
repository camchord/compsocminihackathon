from flask import Flask, render_template, request, redirect
import string_generator as sg
import morse_code

g = sg.generator()

app = Flask(__name__)

@app.route('/')
def index():
    string = g.generate_string()
    template = render_template("index.html", string=string)
    return template

@app.route('/morse')
def morse():
    code = request.args.get('q')
    query = morse_code.translate(code)
    if query:
        return redirect('https://www.google.com/#q=' + query);
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.errorhandler(404)
def go_home(e):
    return redirect('/')
