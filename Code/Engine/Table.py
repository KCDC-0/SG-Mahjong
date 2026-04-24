# class for a full game set


import random
from Tile import Tile, Special_tile

class Table:
    '''A mahjong table that has tiles, can deal tiles, and keeps track of the game state.'''

    def __init__(self, name: str):
        self.name = name
        self.tiles = []

    def __str__(self):
        return f"Table {self.name} with {len(self.tiles)} tiles remaining."
    
    def setup(self):
        '''Sets up the table with a full set of tiles.'''

        self.tiles = []
        for suit in Tile.types['suit']:
            if suit in ['dot', 'bamboo', 'character']:
                for rank in range(1, 10):
                    self.tiles.extend([Tile(suit, rank, 'suited')] * 4)
            elif suit == 'wind':
                for trait in ['east', 'west', 'north', 'south']:
                    self.tiles.extend([Tile(suit, 0, trait)] * 4)
            elif suit == 'dragon':
                for trait in ['green', 'red', 'white']:
                    self.tiles.extend([Tile(suit, 0, trait)] * 4)
        for suit in Special_tile.special_types['suit']:
            for rank in Special_tile.special_types['rank']:
                self.tiles.append(Special_tile(suit, rank, 'special'))

    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.tiles)

    def draw(self):
        '''Pops 1 tile from table'''
        if not self.tiles:
            return None
        return self.tiles.pop()
    
    def deal(self, num):
        '''Deal a specified number of tiles from table'''
        tile_list = []
        for i in range(num):
            tile_list.append(self.tiles.pop())
        return tile_list

    @property
    def tiles_remaining(self):
        '''Returns number of tiles left'''
        return len(self.tiles)