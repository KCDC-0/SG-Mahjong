## The logic control that enforces rules

import sys
sys.path.append('../Engine')
from Tile import Tile, Special_tile
from Table import Table
from Hand import Hand
from Player import Player
import utils

class GameEngine:
    def __init__(self, players: list[Player], table: Table):
        self.players = players
        self.table = table
        self.table.setup()
        self.table.shuffle()
        self.pile = []
        self.current_player_index = 0
        self.current_dealer_index = 0
        self.game_over = False
        self.winners = []

    def __str__(self):
        ret = str(self.table) + '\n'
        for p in self.players:
            ret = ret + str(p) + '\n'
        ret = ret + f'Winners: {str(self.winners)}'
        return ret

    def start_game(self):
        """Initial dealing logic"""
        assert len(self.players) == 4, 'Must have exactly 4 players'

        dir = ['East', 'North', 'West', 'South']
        for i, player in enumerate(self.players):
            player.set_direction(dir[i])
            player.set_tiles(self.table.deal(13))
            while player.hand.tile_hidden_count < 13:
                player.draw_tile(self.table.draw())
            player.hand.sort()
    
    def new_game(self):
        """Starts a new game with existing players and table"""
        assert len(self.winners) > 0, 'Use start_game function for first game'''

        self.table.setup()
        self.table.shuffle()
        self.pile = []
        self.game_over = False
        for i, player in enumerate(self.players):
            player.end_play()
            player.set_tiles(self.table.deal(13))
            while player.hand.tile_hidden_count < 13:
                player.draw_tile(self.table.draw())
            player.hand.sort()

                    
    def play_turn(self):
        """Plays one players full turn"""
        player = self.players[self.current_player_index]

        # Draw
        drawn_tile = self.table.draw()
        if drawn_tile is None:
            self.game_over = True
            return

        player.draw_tile(drawn_tile)

        # Check win (to be added)
        if self.check_win(player):
            self.winners.append(player)
            self.game_over = True
            return

        # Discard (ask for tile function to be added)
        tile_to_discard = player.hand.tiles[0]
        player.discard_tile(tile_to_discard)
        self.pile.append(tile_to_discard)

        # Reactions (pong/chow/kong) (to be added)

        # Next player
        self.current_player_index = (self.current_player_index + 1) % 4

    def check_win(self, player) -> bool:
        """Check if a player had won"""
        # To be added
        return False
    
    def pile_array(self):
        """Returns an array of tiles in the pile"""
        return utils.tile_array(self.pile)