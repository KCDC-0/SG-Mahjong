## extra functions
import numpy as np


tile_encoder = {'bamboo-1': 0,
 'bamboo-2': 1,
 'bamboo-3': 2,
 'bamboo-4': 3,
 'bamboo-5': 4,
 'bamboo-6': 5,
 'bamboo-7': 6,
 'bamboo-8': 7,
 'bamboo-9': 8,
 'character-1': 9,
 'character-2': 10,
 'character-3': 11,
 'character-4': 12,
 'character-5': 13,
 'character-6': 14,
 'character-7': 15,
 'character-8': 16,
 'character-9': 17,
 'dot-1': 18,
 'dot-2': 19,
 'dot-3': 20,
 'dot-4': 21,
 'dot-5': 22,
 'dot-6': 23,
 'dot-7': 24,
 'dot-8': 25,
 'dot-9': 26,
 'dragon-green': 27,
 'dragon-red': 28,
 'dragon-white': 29,
 'wind-east': 30,
 'wind-west': 31,
 'wind-north': 32,
 'wind-south': 33}


def tile_array(tile_list):
    '''Converts a list of tiles into an array for tracking and sending

    Row 1: 
    [0-8]   → bamboo 1-9
    [9-17]  → character 1-9
    [18-26] → dot 1-9
    [27-29] → dragon (G, R, W)
    [30-33] → wind (E, W, N, S)
    '''
    array = np.zeros(34, dtype=int)
    pile = []
    for tile in tile_list:
        if str(tile) in tile_encoder:
            array[tile_encoder[str(tile)]] += 1
        else:
            pile.append(str(tile))
    return array, pile
