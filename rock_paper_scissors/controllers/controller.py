from flask import render_template
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def index():
    return render_template('index.html', title='Rock, Paper, Scissors')

@app.route('/<player1_choice>/<player2_choice>')
def display_winner(player1_choice, player2_choice):
    player1 = Player("player 1", player1_choice)
    player2 = Player("player 2", player2_choice)
    winner = Game.decide_result(Game, player1, player2)
    return render_template("results.html", winner = winner, player1_choice = player1.choice, player2_choice = player2.choice)
    #return winner

@app.route('/play')