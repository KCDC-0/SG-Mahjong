## The logic control that enforces rules
# Game engine class
# Reactions class

import sys
sys.path.append('../Rules')
import win_detection as w
from Reactions import Reaction
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
        self.reaction_phase = False
        self.reactions = []

        self.current_player_index = 0
        self.current_dealer_index = 0
        self.game_over = False
        self.winner = None
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
        self.reactions = []
        self.reaction_phase = False
        self.winner = None
        self.game_over = False
        for i, player in enumerate(self.players):
            player.end_play()
            player.set_tiles(self.table.deal(13))
            while player.hand.tile_hidden_count < 13:
                player.draw_tile(self.table.draw())
            player.hand.sort()

                    
    def play_human_turn(self):
        """Plays one players full turn"""
        player = self.players[self.current_player_index]

        self.draw_stage(self, player)

        if self.game_over:
            return

        # Display tiles in hand (to add)
        
        # ask for user input for discard
        while player.hand.tile_full_count > 13:
            if player.human:
                t_num = 0
                while t_num == 0:
                    try:
                        i_num = int(input('Choose a tile to discard: '))
                
                        if i_num <= len(player.hand.tiles) and i_num > 0:
                            t_num = i_num
                        else:
                            print('please input the number of one of the tiles in your hand')
                    except:
                        print('please input a number')
            
            else:
                t_num = 1

            self.discard_stage(self, player, t_num)

            # Reactions
            for i, other_player in enumerate(self.players):
                if other_player != player and other_player.human:
                    possibilties = self.get_valid_reactions(player, self.table.last_tile)
                    print(possibilties)
                    if len(possibilties) == 0:
                        print(f'No valid reactions for {other_player.direction} player')
                    else:
                        rxn = input('Input a reaction from the valid possibilites above (pong, dchow, mchow, uchow, kong, mahjong). Return any key if no reaction: ')
                        if rxn in possibilties:
                            self.reaction_phase = True
                            self.reactions.append(Reaction(i, rxn))
                else:
                    # bot reactions to be handles later
                    a = 1

            self.reaction_stage()
            player = self.players[self.current_player_index]


        # Next player
        self.reactions = []
        self.current_player_index = (self.current_player_index + 1) % 4

    def draw_stage(self, player):
        #Draw
        drawn_tile = self.table.draw()
        if drawn_tile is None:
            self.game_over = True
            return

        player.draw_tile(drawn_tile)
        self.table.add_last_tile(drawn_tile)

        # Check win
        if self.check_win(player):
            self.winners.append(player)
            self.winner = player
            self.game_over = True
            return
        
    def discard_stage(self, player, tile_num):
        tile_to_discard = player.hand.tiles[tile_num - 1]
        player.discard_tile(tile_to_discard)
        self.pile.append(tile_to_discard)
    
    def reaction_stage(self):
        reactions = self.reactions

        if not reactions:
            return

        reactions.sort(key=lambda r: (-r.priority(), r.player_index))
        chosen = reactions[0]

        self.apply_reaction(chosen)
        
    def apply_reaction(self, reaction):
        player = self.players[reaction.player_index]
        tile = reaction.tile

        if reaction.action == "hu":
            self.state.winner = player
            self.state.game_over = True
            return

        elif reaction.action == "pong":
            player.make_meld([self.table.last_tile] * 3)

        elif reaction.action == "kong":
            player.make_meld([self.table.last_tile] * 4)

        elif reaction.action == "chow":
            # to implement
            a = 1
        
        self.reaction_phase = False
        self.current_player_index = reaction.player_index

    def get_valid_reactions(self, player, tile):
        '''Returns a list of valid reactions for a player'''

        actions = []

        # to be implemented
        if self.can_win(player, tile):
            actions.append("mahjong")

        if self.can_pong(player, tile):
            actions.append("pong")

        if self.can_kong(player, tile):
            actions.append("kong")

        # chow only for next player
        if self.can_down_chow(player, tile):
            actions.append("dchow")

        if self.can_middle_chow(player, tile):
            actions.append("mchow")

        if self.can_up_chow(player, tile):
            actions.append("uchow")

        return actions
    





    def can_pong(self, player, tile):
        # to implement
        pass


    def can_down_chow(self, player, tile):
        # to implement
        pass

    def can_middle_chow(self, player, tile):
        # to implement
        pass

    def can_up_chow(self, player, tile):
        # to implement
        pass


    def can_kong(self, player, tile):
        # to implement
        pass

    def check_win(self, player) -> bool:
        """Check if a player had won"""

        return w.is_win(utils.tile_array(player.hand.tiles))
    
    def pile_array(self):
        """Returns an array of tiles in the pile"""
        return utils.tile_array(self.pile)