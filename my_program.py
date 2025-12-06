from mymath import basic_math
from mymath import geometry


option1 = input("Do you want to perform basic math operation?(yes or no)")

if option1 == "yes":
  a = int(input("enter 1st number: "))
  b = int(input("enter 2nd number: "))
  add = basic_math.addition(a , b)
  sub = basic_math.subtraction(a , b)
  mul = basic_math.multiply(a , b)
  div = basic_math.divide( a, b)
  rem = basic_math.reminder( a , b)
  print(f"Addition: {add} , Subtractio : {sub} , Multiply: {mul} , division : {div} , reminder: {rem}")

elif option1 == "no":
  print("OKAYY")

option2 = input("Do you want to perform geometry?(yes or no) : ")
if option2 == "yes":
  r = int(input("enter radius: "))
  geometry.area_circle(r)
  length = int(input("enter length of square: "))
  geometry.area_sq(length)
  l = int(input("enter length of rectangle: "))
  b = int(input("enter breadth of rectangle: "))
  geometry.area_rec(l , b)
    
else:
  print("Okayy")
