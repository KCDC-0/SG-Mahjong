## Used for testing the rukes of the game

import sys
sys.path.append('../Rules')
import Control as c
sys.path.append('../Engine')
from Tile import Tile, Special_tile
from Table import Table
from Hand import Hand
from Player import Player
import utils

def test_game_set():
    '''Used to test a complete game setup and play 1 round'''
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
