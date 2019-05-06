from flask import Flask, render_template
from main import app

@app.route('/how-to-dos')
def how_dos_page():
    return render_template('how-to-dos/how-to-dos.html')

@app.route('/how-to-dos/ping-flood')
def ping_flood_page():
    return render_template('how-to-dos/ping-flood.html')

@app.route('/how-to-dos/slowloris')
def slowloris_page():
    return render_template('how-to-dos/slowloris.html')