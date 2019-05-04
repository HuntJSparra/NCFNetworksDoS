from flask import Flask, render_template
from main import app

@app.route('/what-is-dos')
def dos_page():
    return render_template('what-is-dos.html')

@app.route('/what-is-dos/buffer-overflow')
def buffer_overflow_page():
    return 'Buffer Overflow'

@app.route('/what-is-dos/icmp-flood')
def icmp_flood_page():
    return 'ICMP Flood'

@app.route('/what-is-dos/syn-flood')
def syn_flood_page():
    return 'SYN Flood'

@app.route('/what-is-dos/ddos')
def ddos_page():
    return 'DDoS'