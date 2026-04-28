## Human player class

from Hand import Hand
from Tile import Tile

class Player:
    def __init__(self, name: str):
        self.name = name
        self.discards = []
        self.direction: str
        self.hand = Hand()
        self.cash = 0

    def __str__(self):
        return f"Player({self.name}): {self.direction}, ${self.cash}"

    def set_direction(self, dir: str):
        '''Sets a table direction for a player'''
        if dir in ['North', 'South', "East", 'West']:
            self.direction = dir
        else: return False

    def set_tiles(self, tiles: list):
        '''Draws tiles and adds it to hand, used for start of game'''
        if self.hand.tile_hidden_count == 0:
            self.hand.add_tiles(tiles)
        else:
            return False
    
    def end_play(self):
        '''Resets the players hand, used for ending a game'''
        self.discards = []
        self.hand.empty_hand()
    
    def draw_tile(self, tile: Tile):
        '''Draws a chosen tile and adds it to hand'''
        self.hand.add_tile(tile)

    def discard_tile(self, tile: Tile):
        '''Discards a chosen tile from hand'''
        if tile in self.hand.tiles:
            self.hand.discard_tile(tile)
            self.discards.append(tile)
            return tile
        else:
            return False
    
    def make_meld(self, tiles):
        '''Makes a chosen meld from hand'''
        self.hand.sort()
        tiles.sort(key=lambda t: (t.suit, t.rank))
        index = 0
        for t in self.hand.tiles:
            if t == tiles[index]:
                index += 1
        if index >= len(tiles):
            self.hand.add_meld(tiles)
        else:
            return False
            
    
    def add_cash(self, amount: int):
        '''Tops up chips by specified amount'''
        self.cash += amount
