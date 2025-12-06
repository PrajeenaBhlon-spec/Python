class reverse_iterator:
  def __init__(self , word):
    self.word = word
    self.array = list(self.word)
    self.end = len(self.word) - 1
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.end < 0:
      raise StopIteration
    value = self.end
    self.end -= 1 
    return self.array[value]
  
  def display(self):
    print(self.array)

#rev = reverse_iterator("prajeena")
r = reverse_iterator("prajeena")
for i in r:
  print(i , end="")

