## Used for testing the core engine

# from Engine.Tile import Tile, Special_tile

import sys
sys.path.append('../Engine')
from Tile import Tile, Special_tile
from Table import Table
import utils

def test_add_tile():
    '''test if tiles and special tiles work and can be tested for validity'''

    temp_hand = []  # temporary hand, before implementation of hand class
    temp_hand.append(Tile("bamboo", 3, 'suited'))
    temp_hand.append(Tile("dot", 3, 'red'))
    temp_hand.append(Tile("flower", 4, "special"))
    temp_hand.append(Tile("wind", 0, "green"))
    temp_hand.append(Special_tile("flower", 2, "suited"))
    temp_hand.append(Special_tile("animal", 1, "special"))

    for tile in temp_hand:
        if tile.valid_tile == True:
            print(tile)

def test_set_table():
    '''test if a full table can be set up and tiles can be dealt'''
    table1 = Table('1')
    table1.setup()
    table1.shuffle()
    print(table1)
    table1.draw()
    print(table1)
    table1.deal(5)
    print(table1)

def test_array():
    '''test if a table can be reprented by an array'''
    table1 = Table('1')
    table1.setup()
    table1.shuffle()
    table1.draw()
    table1.deal(5)
    return utils.tile_array(table1.tiles)

