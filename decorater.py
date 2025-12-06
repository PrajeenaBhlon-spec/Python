
def info_decorator(func):
  def after_decoration(*args , **kwargs):
    print(f"You have called the {func.__name__} function")
    print("the argument passed:")
    for key,value in kwargs.items():
      print(f"{key} = {value}")
    func(*args , **kwargs)
    print("Thank you for using this fucntion")
  return after_decoration

@info_decorator
def introduction(name , age , address ):
  print(f"hello my name is {name} and i am {age} years old. I live in {address}" )
  print(" ")

introduction(name="prajeena",age=22,address="padampokhari")



def repeater(fx):
  def decoration(*args,**kwargs):
    i = int(input("enter interation amount: "))
    print("Iteration beginss!!")
    while i > 0:
      fx(*args,**kwargs)
      i -= 1
    print("Iteratiom completee!")
  return decoration

@repeater
def statement(name):
  print(f"{name} is a diva")

statement("tinku")

def type_check_decorator(fx):
  def mfx(*args , **kwargs):
    result = []
    for item in args:
      if type(item) == int:
        result.append(True) 
      else:
        result.append(False)
    
    
    if all(result):
      print("All arguments are of int type")
      print("processing can be done")
      fx(*args , **kwargs)
    else:
      print("not valid arguments")
      return
  return mfx
        
      
@type_check_decorator
def operation(a , b):
  print(a+b)

operation(2 , 3)
operation("fnckd" , 8)