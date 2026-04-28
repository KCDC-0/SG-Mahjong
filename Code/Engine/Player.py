## Human player class

from Hand import Hand
from Tile import Tile

class Player:
    def __init__(self, name: str):
        self.name = name
        self.discards = []
        self.hand = Hand()
        self.cash = 0

    def __str__(self):
        return f"Player({self.name}): ${self.cash}"

    def draw_tile(self, tile: Tile):
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
