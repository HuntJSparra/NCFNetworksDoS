from flask import Flask, render_template
from main import app

@app.route('/what-is-dos')
def what_dos_page():
    return render_template('what-is-dos/what-is-dos.html')

@app.route('/what-is-dos/buffer-overflow')
def buffer_overflow_page():
    return render_template('what-is-dos/buffer-overflow.html')

@app.route('/what-is-dos/ddos')
def ddos_page():
    return render_template('what-is-dos/ddos.html')