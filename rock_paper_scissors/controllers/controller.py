from flask import render_template
from app import app
# from models.game import *
# from models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Rock, Paper, Scissors')

# @app.route('/<player1_choice>/<player2_choice>')
# def display_winner(player1_choice, player2_choice):
    