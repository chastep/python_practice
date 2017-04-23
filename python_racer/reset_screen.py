# import subprocess
import os

def reset_screen():
  clear_screen()
#   move_to_home()
# Clears the content on the screen.
def clear_screen():
  os.system('clear')
#   print(chr(27) + "[2J")
# # Moves the insert point in the terminal back to the upper left.
# def move_to_home():
#   print(chr(27) + "[H")

