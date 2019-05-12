from flask import Flask, render_template
from main import app

@app.route('/how-to-stop-dos')
def how_stop_page():
    return render_template('how-to-stop-dos/how-to-stop-dos.html')

@app.route('/how-to-stop-dos/slow-loris')
def stop_slow_loris_page():
    return render_template('how-to-stop-dos/slow-loris.html')

@app.route('/how-to-stop-dos/ping-flood')
def stop_ping_flood_page():
    return render_template('how-to-stop-dos/ping-flood.html')