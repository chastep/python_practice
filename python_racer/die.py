from random import randint
class Die:
  # make an instance variable tied to the die reflecting side count
  def __init__(self, side_count):
    self.side_count = side_count
  # roll method for die
  # returns random number between 1-side count
  def roll(self):
    return randint(1, self.side_count)
