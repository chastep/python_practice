from random import randinit
class Die:
  def __init__(self, side_count):
    self.side_count = side_count
  # roll method for die
  # returns random number between 1-side count
  def roll(self):
    return randinit(1, self.side_count)
