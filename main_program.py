from games import tictactoe
from games import numberguess

print("GAME OPTIONS:")
print("1.Number guess game")
print("2.Tic tac toe")
print("3.dice roll game")
option = input("choose one: ")
if option == '2':
  tictactoe.play()
elif option == '1':
  numberguess.play_guess()