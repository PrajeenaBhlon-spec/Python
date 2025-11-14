import random

def play_guess():
  num_range = range(101)
  comp_choice = random.choice(num_range)

  user_ans = int(input("guess a number between 0 to 100: "))
  if user_ans == comp_choice:
    print("you winnn")
    
  else:
    count = 5
    while user_ans != comp_choice:
      count -= 1
      print(f"you have {count} chance left")
      if count <= 0:
        print("game overr. you losee!!!")
        break
      user_ans = int(input("guess a number between 0 to 100: "))

    if user_ans == comp_choice:
      print("you winnn")
  
  