def greet(fx):
  def mfx(*args):
    print("Hello user!!")
    fx(*args)
    
  return mfx


def addition(a , b):
   return a + b

def subtraction(a , b):
   return a - b


def multiply(a , b):
  return a * b


def divide(a , b):
   return a / b


def reminder(a , b):
  return a % b