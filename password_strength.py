

class weakPasswordError(Exception):
  def __init__(self , message):
    self.message = message
    super().__init__(message)

  

try: 
  password = input("enter your password: ")
  special_char = "!@#$%^&*"
  number = "0123456789"
  if len(password) >= 8:
    count_of_special = 0
    count_of_number = 0
    for char_special in password:
      for special in special_char:
        if char_special == special:
          count_of_special += 1
    
    for char_num in password:
      for num in number:
        if char_num == num:
          count_of_number += 1
    
    if count_of_number == 0 and count_of_special == 0:
      raise weakPasswordError("password is weak with no special characters and numbers")
    else:
      print("Your password is strong")


  else:
    raise weakPasswordError("password length is less than 8")
  
except weakPasswordError as e:
  print(e)
