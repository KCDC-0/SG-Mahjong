## Used for testing the rukes of the game

import sys
sys.path.append('../Rules')
import Control as c
import win_detection as w
sys.path.append('../Engine')
from Tile import Tile, Special_tile
from Table import Table
from Hand import Hand
from Player import Player
import utils

def test_game_set():
    '''Used to test a complete game setup and play 1 turn'''
    table1 = Table('1')
    players = []
    for i in range(1, 5):
        p = Player(str(i))
        players.append(p)
        p.add_cash(50)
    game1 = c.GameEngine(players, table1)
    game1.start_game()
    game1.play_turn()
    print(game1)
    for p in game1.players:
        print(p.hand)
    return utils.tile_array(game1.table.tiles), game1.pile_array()

def test_win_detection():
    '''Used to test the win detection function'''
    winner = [1, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0]
    loser = [1, 1, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0]
    winner_13 = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
         0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1]
    
    return w.is_win(winner), w.is_win(loser), w.is_win(winner_13)

def test_play_round():
    '''Used to test dealing, reactions and 1 round of play'''
    table1 = Table('1')
    players = []
    for i in range(1, 5):
        p = Player(str(i))
        players.append(p)
        p.add_cash(50)
    game1 = c.GameEngine(players, table1)
    game1.start_game()
    game1.play_human_turn()
    game1.play_human_turn()
    game1.play_human_turn()
    game1.play_human_turn()

def test_full_game():
    '''Used to test 1 full human game'''
    # to be added


