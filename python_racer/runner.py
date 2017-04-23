import subprocess
import time
from die import Die
from python_racer import PythonRacer
from reset_screen import reset_screen

sides = eval(input("How big of a die to you want?"))
die = Die(sides)
length = eval(input("How far are we going?"))
players = ['a', 'b']
game = PythonRacer(players, die, length)
reset_screen()
game.board_visualization()
time.sleep(2)

while game.finished() == False:
  reset_screen()
  for player in game.players:
    game.advance_player(player)
  game.board_visualization()
  time.sleep(.25)

game.winner()