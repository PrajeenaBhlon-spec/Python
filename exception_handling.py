

try:
  a = int(input("enter numerator: "))
  b = int(input("enter denominator: "))
  result = a / b
  print(result)

except ZeroDivisionError:
  print("divide by 0 cannot be done")



person = {
  "name": "prajeena",
  "age" : 21 
}
try:
  print(person['address'])
except KeyError:
  print("key doesnot exist")