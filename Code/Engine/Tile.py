## tile class

from dataclasses import dataclass

@dataclass(frozen=True)
class Tile:
    '''A mahjong tile that has a suit, rank and/or trait'''
    types = {'suit':  ['dot', 'bamboo', 'character', 'dragon', 'wind'],
            'rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 
            'trait': ['suited', 'green', 'red', 'white', 'east', 'west', 'north', 'south']
            }

    suit: str
    rank: int
    trait: str

    def __str__(self):
        if self.rank != None:
            return f"{self.suit}-{self.rank}"
        else:
            return f"{self.suit}-{self.trait}"

    @property
    def is_suited(self):
        '''Returns if a tile is suited or not'''
        return self.trait == 'suited'
    
    @property
    def valid_tile(self):
        '''Returns if a tile is a valid mahjong tile or not'''
        if self.suit in ["bamboo", "character", "dot"]:
            return self.rank != 0 and self.trait == 'suited' and self.rank in self.types['rank']
        elif self.suit == 'wind':
            return self.rank == 0 and self.trait != 'suited' and self.trait in ['east', 'west', 'north', 'south']
        elif self.suit == 'dragon':
            return self.rank == 0 and self.trait != 'suited' and self.trait in ['green', 'red', 'white']


@dataclass(frozen=True)
class Special_tile(Tile):

    special_types = {'suit':  ['flower', 'season', 'animal'],
                    'rank': [1, 2, 3, 4]}
    animal_correspondence = {1: ['cat', 1], 2: ['mouse', 0], 3: ['rooster', 1], 4: ['centipede', 0]}

    @property
    def valid_tile(self):
        '''Returns if a special tile is a valid mahjong tile or not'''
        return self.suit in self.special_types['suit'] and self.rank in self.special_types['rank'] and self.trait == 'special'
    

