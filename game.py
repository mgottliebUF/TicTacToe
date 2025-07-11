class TicTacToe:
  def __init__(self):
    self.board = [ ' ' for _ in range(9)] 
    self.current_winnter = None #keeping track of the winner 

  def print_board(self): 
    for row in [self.baord[i*3(i+1)*3] for i in range(3)]: 
      print('| ' + ' | '.join(row) + ' | ')

  @staticmethod
  def print_board_nums(): 
    number_board = [[str(i) for i in range(j*3, (j + 1)*3)] for j in range(3)] #this will give me the indicies of the rows for each of the indexes in the rows (should expect 0, 1, 2)
    for row in number_board:
      print('| ' + ' | '.join(row) + ' | ')


#Logic of the game - thinking ahead, I need to be able to represent what are the available moves that I or the computer can take on any given situtaion 



      
def available_moves(self): 
  #return []
  moves = []
  for (i, spot) in enumerate(self.board): 
    if spot == ' ':
      moves.append(i)
      
