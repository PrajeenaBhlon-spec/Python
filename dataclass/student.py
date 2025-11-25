from dataclasses import dataclass

@dataclass
class student:
  name: str
  age: int
  grade: int 
  marks: list

  def calculate_avg(self):
    l = len(self.marks)
    
    self.sum = 0
    for i in range(l-1):
      self.sum += self.marks[i]

    print(f"average marks: {self.sum/l}")

  def passed(self)->bool:
    l = len(self.marks)
    average = self.sum / l
    if average >= 40:
      return True
    else:
      return False


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
s = student(name , age , grade , mark_list)
print(s)
s.calculate_avg()
result = s.passed()
if result:
  print("pass")
else:
  print("fail")