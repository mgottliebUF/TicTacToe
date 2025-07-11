import math 
import random 

class Player: 
  def __init__(self, letter):
    self.letter = letter 

  def get_move(self, game): 
    pass 

class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game): 
      square = random.choice(game.available_moves())
      return square #This gets a random available spot

class HumanPlayer(Player):
  def __init__(self, letter): 
    super().__init__(letter)

  def get_move(self, game): 
    valid_square = False
    val = None
    while not valid_square: 
      square = input(self.letter + '\'s turn. Input move(0-9):')
      try: #implementing checks to ensure user isn't violating rules of the game.
        val = int(square)
  
