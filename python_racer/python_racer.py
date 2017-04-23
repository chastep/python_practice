class PythonRacer:

  def __init__(self, players, die, length = 30):
    self.die = die
    self.players = players
    self.length = length
    self.players_positions = { players[0]: 0, players[1]: 0 }

  # Returns +true+ if one of the players has reached
  # the finish line, +false+ otherwise
  def finished(self):
    if self.players_positions[self.players[0]] >= self.length - 1:
      return True
    elif self.players_positions[self.players[1]] >= self.length - 1:
      return True
    else:
      return False

  # Returns the winner if there is one, +nil+ otherwise
  def winner(self):
    if self.players_positions[self.players[0]] == self.length - 1 and self.players_positions[self.players[1]] == self.length - 1:
      print("It's a tie!!!")
    elif self.players_positions[self.players[0]] >= self.length - 1:
      print("The winner is player " + self.players[0] + "!!!")
    elif self.players_positions[self.players[1]] >= self.length - 1:
      print("The winner is player " + self.players[1] + "!!!")
      return self.players[1]
    
  # Rolls the die and advances +player+ accordingly
  def advance_player(self, player):
    self.players_positions[player] += self.die.roll()
    if self.players_positions[player] >= self.length:
       self.players_positions[player] = self.length - 1

  # Returns the current state of the game as a string
  # that can be printed on the command line.
  # The board should have the same dimensions each time.
  def board_visualization(self):
    player1_track = [' '] * self.length
    player2_track = [' '] * self.length
    player1_track[self.players_positions[self.players[0]]] = self.players[0]
    player2_track[self.players_positions[self.players[1]]] = self.players[1]
    print('| '.join(player1_track))
    print('| '.join(player2_track))


