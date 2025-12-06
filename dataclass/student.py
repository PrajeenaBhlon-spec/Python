from dataclasses import dataclass

@dataclass
class student:
  name: str
  age: int
  grade: int 
  marks: list
  average : float
  status : bool

  def calculate_avg(self):
    l = len(self.marks)
    
    self.sum = 0
    for i in range(l-1):
      self.sum += self.marks[i]
    self.average = self.sum / l
    print(f"average marks: {self.average}")

  def passed(self)->bool:
    l = len(self.marks)
    average = self.sum / l
    if average >= 40:
      self.status = True
      return True
    else:
      self.status = False
      return False
  def __str__(self):
    return f"Student(name = {self.name} , age={self.age}, grade={self.grade} , average:{self.average} , status: {self.status})"

name = input("enter student name: ")
age = int(input("enter age: "))
grade = int(input("enter grade: "))
mark_list = []
math = int(input("math marks: "))
mark_list.append(math)
science = int(input("science marks: "))
mark_list.append(science)
nepali = int(input("mepali marks: "))
mark_list.append(nepali)
eng = int(input("english marks: "))
mark_list.append(eng)
social = int(input("social marks: "))
mark_list.append(social)
avg = 0
stat = None
s = student(name , age , grade , mark_list , avg , stat)
s.calculate_avg()
result = s.passed()
if result:
  print("pass")
else:
  print("fail")

print(s)