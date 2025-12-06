
def fibo_generator(r):
  a = 0
  b = 1
  yield 0
  yield 1
  for i in range(r):
    new  = a + b
    if new > r:
      break
    else:
      yield a + b 
      a = b 
      b = new
    i = i + 1

range_of_series = int(input("enter your preferred range: "))
for i in fibo_generator(range_of_series):
  print(i)