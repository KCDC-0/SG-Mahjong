## Used for testing the core engine

from Engine.Tile import Tile, Special_tile

def test_add_tile():
    'test if tiles and special tiles work and can be tested for validity'

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
