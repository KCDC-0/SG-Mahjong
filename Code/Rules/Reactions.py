# engine/reaction.py

class Reaction:
    def __init__(self, player_index, action):
        self.player_index = player_index
        self.action = action 

    def priority(self):
        priorities = {
            "mahjong": 3,
            "kong": 2,
            "pong": 2,
            "mchow": 1,
            "uchow": 1,
            "dchow": 1,
            "chow": 1
        }
        return priorities[self.action]
    
'''
Player 1 turn:
    draw
    discard

→ Reaction phase:
    other players may react

IF no reaction:
    next player (B)

IF pong/kong/chow:
    reacting player takes turn
    IF pong/chow:
        return to discard stage
    IF kong:
        return to draw phase for next player

IF mahjong:
    game ends
'''