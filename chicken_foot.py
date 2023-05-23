from copy import deepcopy
import csv
import random
from typing import Dict, List, Tuple
from domino import Domino
from linked_list import ChickenFootLine, LineNode
from random import randrange

# Do not modify; this is used by the tests
class PossibleMove:
    def __init__(self, target_line: ChickenFootLine, target_line_name:str, domino:Domino) -> None:
        self.target_line = target_line
        self.target_line_name = target_line_name
        self.domino = domino

# Chicken Foot Dominos
# *************************************
# See OneNote for game information
# 
# Instructions
# 1) Implement/Customize the ChickenFootLine class on linked_list.py. This is a specialized linked list for the game.  
#    It does not have to include standard linked list functions and can be custom to what you need. Add attributes or 
#    methods as needed, as long as it still uses nodes and pointers to connect elements.
#
# 2) Customize the Domino class to meet your needs (suggested helpers are stubbed; add methods and attributes that will help you)
#
# 3) Implement the ChickenFoot class to run a game of chicken foot, using ChickenFootLine
# 
# Extension: Use Pygame or Tkinter to create an interactive UI for the game that calls the APIs
# You will likely need to modify these APIs with the following: 
# a) start_game: Generate a "chicken yard" with all the dominos with all combinations up to max_pips
# b) start_game: If dominos_dealt is None, pick a random 7 dominos for each player from the "chicken yard"
# c) draw_domino: If domino is None, draw a random tile from the chicken yard you generated in (a). End the 
# game if there are no more tiles
# d) Add an API to calculate the score of each player.  Score is the sum of pips on remaining tiles in hand (lowest is best) 

class ChickenFoot:

    # num_players: the number of players playing the game
    # max_pips: the largest number of pips (dots) on a side of a domino
    def __init__(self, num_players: int, max_pips: int) -> None:
        self.num_players = num_players
        # self.played = 0
        self.max_pips = max_pips
        self.lines = []
        self.lines_unfilled = []
        self.curr_player_index = 0
        


    # Starts a game of dominos using the starting double number
    # starting_pips: the number of pips for the starting double domino (e.g. 7 would be passed for a 7-7 in the center)
    # dominos_dealt: a list of starting hand for all players, where each hand is a list of Domino objects.  
    def start_game(self, starting_pips:int, dominos_dealt: List[List[Domino]] = None) -> None:
        self.starting_pips = starting_pips
        self.dominoes_dealt = dominos_dealt
        ln = LineNode(Domino(starting_pips,starting_pips))
        ln.domino.set_open_value(starting_pips)
        for i in range(6):
            line = ChickenFootLine(ln, str(ln.domino))
            self.lines.append(line)
            self.lines_unfilled.append(line)
       
    # Finds and returns a list of PossibleMove objects representing possible moves that the current player can make
    # based on tiles in their hand and what is open on the board (see object definition above) 
    def find_moves(self) -> List[PossibleMove]:
        possible_moves = []
        #traverse the 6 ChickenFoot lines made from beginning domino
        if len(self.lines_unfilled) >0:
            # while self.dominoes_dealt[self.curr_player_index]:
            for d in self.dominoes_dealt[self.curr_player_index]:
                for i in self.lines_unfilled:
                    if d.contains_val(i.first.domino.open_value):
                        pm = PossibleMove(i,i.line_name, d)
                        possible_moves.append(pm)
                        
        else:
            for d in self.dominoes_dealt[self.curr_player_index]:
                for i in self.lines:
                    if d.contains_val(i.first.domino.open_value):
                        pm = PossibleMove(i,i.line_name, d)
                        possible_moves.append(pm)
                        
                
        return possible_moves

    # Draws the specified domino from the pile into the current player's hand
    # domino: the domino that the user picked from the pile.  
    def draw_domino(self, domino:Domino = None) -> Domino:
        self.dominoes_dealt[self.curr_player_index].append(domino)
    
    # Place specified domino on the head of the place linked list
    # domino: the domino to place
    # place: a linked list of dominos on a path on the board
    def place_domino(self, domino:Domino, place:ChickenFootLine) -> None:
        new_node = LineNode(domino)
        #if place.first.domino.open_value == domino.value[0]:
        domino.set_open_value(place.first.domino.open_value)
        place.add(domino)
        if domino.is_double():
            for i in range(2):
                cfl = ChickenFootLine(LineNode(domino), place.line_name)
                self.lines_unfilled.append(cfl)
                self.lines.append(cfl)

        if place in self.lines_unfilled:
            self.lines_unfilled.remove(place)

    # Moves on to the next player
    def end_turn(self) -> None:
        if self.curr_player_index < self.num_players-1:
            self.curr_player_index+=1
        else:
            self.curr_player_index = 0

    # Return a list of strings that represent all paths on the board (same string as the target_line_name), 
    # with the center double of the board as the last one. Paths are represented with hyphens between numbers on a single domino, 
    # and | between dominos.  e.g. A path on a board with a double 12 in the center looks like this: 
    # "7-2|2-2|2-5|5-6|6-6|6-1|1-12|12-12"
    def get_board_paths(self) -> List[str]:
        board_paths_str = []
        for i in self.lines:
            line_str = i.line_name
            board_paths_str.append(line_str)

        return board_paths_str