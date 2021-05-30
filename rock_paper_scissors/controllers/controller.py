from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def index():
    return render_template('index.html', title='Rock, Paper, Scissors')

@app.route('/<player1_choice>/<player2_choice>')
def display_winner(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    winner = Game.decide_result(Game, player1, player2)
    return render_template(
        "results.html", 
        winner = winner, 
        player1_name = player1.name,
        player2_name = player2.name, 
        player1_choice = player1.choice, 
        player2_choice = player2.choice
        )
    #return winner

@app.route('/play')
def play():
    return render_template("play.html", title="Vs Cpu")

@app.route('/results', methods=['POST']) 
def play_vs_cpu():
    player_name = request.form.get('name')
    player_move = request.form.get('move')
    human_player = Player(player_name, player_move)
    cpu_player = Game.create_cpu(Game)
    winner = Game.decide_result(Game, human_player, cpu_player)
    return render_template(
        "results.html", 
        winner = winner, 
        player1_name = human_player.name,
        player2_name = cpu_player.name,
        player1_choice = human_player.choice, 
        player2_choice = cpu_player.choice 
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        "404.html",
        title= "Woops!"
    ), 404



