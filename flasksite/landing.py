from flask import Flask, render_template
from main import app

@app.route('/')
def landing_page():
    return render_template('home.html')