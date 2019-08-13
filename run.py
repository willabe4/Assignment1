from flask import Flask, render_template
app = Flask(__name__)

info = [
    'Character Name',
    'Race',
    'Class'

]

@app.route('/')
def index():
    return render_template('index.html', info=info)
