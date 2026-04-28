# hand class
from Tile import Tile, Special_tile

class Hand:
    def __init__(self):
        self.tiles = []
        self.melds = []
        self.special = []

    def __str__(self):
        ret_1 = ", ".join(str(t) for t in self.tiles)
        ret_2 = ""
        for m in self.melds:
            temp = ", ".join(str(t) for t in m)
            ret_2 = ret_2 + temp + '\n'
        ret_3 = ", ".join(str(t) for t in self.special)
        return ret_1 + '\n' + ret_2 + '\n' + ret_3
    
    def empty_hand(self):
        '''Removes all tiles in hand, used to reset hand between games'''
        self.tiles = []
        self.melds = []
        self.special = []

    def add_tiles(self, tile_list: list):
        '''Adds a given list of tiles to the hand'''
        for tile in tile_list:
            if tile.trait == 'special':
                self.special.append(tile)
            else:
                self.tiles.append(tile)

    def add_tile(self, tile: Tile):
        '''Adds a given tile to the hand'''
        if tile.trait == 'special':
            self.special.append(tile)
        else:
            self.tiles.append(tile)

    def discard_tile(self, tile: Tile):
        '''Removes a given tile from the hand'''
        self.tiles.remove(tile)

    def sort(self):
        '''Sorts hidden tiles in the hand'''
        self.tiles.sort(key=lambda t: (t.suit, t.rank))

    def add_meld(self, tile_list: list):
        '''Forms 1 meld of tiles given the tiles in the meld'''
        for tile in tile_list:
            assert tile in self.tiles, "Tiles listed not in hand"
            self.tiles.remove(tile)
        self.melds.append(tile_list)

    @property
    def tile_hidden_count(self):
        '''Returns a count of hidden tiles'''
        return len(self.tiles)
    
    @property
    def tile_full_count(self):
        '''Returns a count of non-special tiles, adjusting for kong melds'''
        return len(self.tiles) + len(self.melds) * 3