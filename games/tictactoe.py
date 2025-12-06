import random
import time

position = [["" , "" , ""],
            ["" , "" , ""],
            ["" , "" , ""]]


already_guessed = []
row = [ 0 , 1 , 2]
column = [0 ,1 , 2]

def check_comp_win(position , move , comp_choice):
  if position[0][0]== comp_choice and position[1][1] == comp_choice and position[2][2] == comp_choice:
    for line in position:
      print(line)
    print("computer wins")
    return True
    
  elif position[0][0]== comp_choice and position[0][1] == comp_choice and position[0][2] == comp_choice:
    
    for line in position:
     print(line)
    print("computer wins")
    return True
    
  elif position[0][0]== comp_choice and position[1][0] == comp_choice and position[2][0] == comp_choice:
    for line in position:
     print(line)
    print("computer wins")
    return True
    
  elif position[0][0]== comp_choice and position[0][1] == comp_choice and position[0][2] == comp_choice:
    
    for line in position:
      print(line)
    print("computer wins")
    return True
    
  elif position[2][0]== comp_choice and position[1][1] == comp_choice and position[0][2] == comp_choice:
    for line in position:
      print(line)
    
    print("computer wins")
    return True
    
  elif position[0][0]== comp_choice and position[0][1] == comp_choice and position[0][2] == comp_choice:
    
    for line in position:
      print(line)
    print("computer wins")
    return True
  elif position[0][2]== comp_choice and position[1][2] == comp_choice and position[2][2] == comp_choice:
    for line in position:
      print(line)
    
    print("computer wins")
    return True
  elif position[2][0]== comp_choice and position[2][1] == comp_choice and position[2][2] == comp_choice:
    
    for line in position:
      print(line)
    print("computer wins")
    return True
  elif position[1][0]== comp_choice and position[1][1] == comp_choice and position[1][2] == comp_choice:
    for line in position:
      print(line)
    print("computer wins")
    return True
  

def check_user_win(position , move , comp_choice):
  if position[0][0]== move and position[1][1] == move and position[2][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
    
  elif position[0][0]== move and position[0][1] == move and position[0][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
    
  elif position[0][0]== move and position[1][0] == move and position[2][0] == move:
    for line in position:
      print(line)
    print("You win")
    return True
    
  elif position[0][0]== move and position[0][1] == move and position[0][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
    
  elif position[2][0]== move and position[1][1] == move and position[0][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
    
  elif position[0][0]== move and position[0][1] == move and position[0][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
  elif position[0][2]== move and position[1][2] == move and position[2][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
  elif position[2][0]== move and position[2][1] == move and position[2][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
  elif position[1][0]== move and position[1][1] == move and position[1][2] == move:
    for line in position:
      print(line)
    print("You win")
    return True
  


def play():
  move = input("are you x or o? ")
  if move == 'o':
    comp_choice = 'x'
  else:
    comp_choice = 'o'

  for i in range(20):
    print(f"past moves: {already_guessed}")
    print("choose position for your move:")
    i = int(input("enter: "))
    j = int(input("enter: "))
  
    position[i][j] = move
    result1 = check_user_win(position , move , comp_choice)
    if result1:
      break
    for line in position:
      print(line)
    already_guessed.append(str(i)+str(j))
  
    time.sleep(3)

    comp_i = random.choice(row)
    comp_j = random.choice(column)
    print(f"computer choosed: {str(comp_i)+str(comp_j)}")

    while str(comp_i)+str(comp_j) in already_guessed:
      comp_i = random.choice(row)
      comp_j = random.choice(column)

    result2 = check_comp_win(position , move , comp_choice)
    if result2:
      break
    already_guessed.append(str(comp_i)+str(comp_j))
    position[comp_i][comp_j] = comp_choice
    time.sleep(2)
    for line in position:
      print(line)


