class num_iterator:
  def __init__(self , numList):
    self.numList = numList
    self.end = len(numList)-1
    self.start = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    current_val = self.start
    if current_val > self.end:
      raise StopIteration
    
    self.start += 1
    return pow(self.numList[current_val] , 2)
  def display(self):
    print(self.end)

    
numbers = [2 , 4 , 5 , 7 ,34 , 13]
square_result = num_iterator(numbers)
for i in square_result:
  print(i)
