"""class dog:
  def __init__(self , name ,age):
    self.name = name 
    self.age = age

  def bark(self):
    print(self.name + " barks")
    print(self.name + " is " + str(self.age) + " years old")

d1 = dog("bony" , 5)
d2 = dog("lucky" , 2)
d1.bark()
d2.bark()"""

"""class student:
  def __init__(self , name , age , grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade
  
class course:
  def __init__(self , name , max_students):
    self.name = name
    self.max_students= max_students
    self.students = []

  def add_students(self , student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    else:
      return False
    

  def get_average_grade(self):
    value = 0
    for stu in self.students:
      value += stu.get_grade()

    return value / len(self.students)

s1 = student("prajeena" , 22 , 99)
s2 = student("pramila" , 24 , 89)
s3 = student("sarswoti" , 24 , 80)
c1 = course("science" , 2)
print(c1.add_students(s1))
print(c1.add_students(s2))
print(c1.students[0].name)
print(c1.students[0].age)
print(c1.get_average_grade())
print(c1.add_students(s3))"""


"""class pet:
  def __init__(self, name , age):
    self.name = name 
    self.age = age
  def show(self):
    print(f"I am {self.name} and I am {self.age} years old" ) 

class cat(pet):
  def __init__(self , name , age , color):
    super().__init__(name , age)
    self.color = color

  def speak(self):
    print("meow")

class dog(pet):
  def speak(self):
    print("bark")


p = pet("lucky" , 4)
p.show()
print("")
c = cat("bubble" , 10 , "orange")
c.show()
c.speak()
print("")
d=dog("bony" , 6)
d.show()
d.speak()"""

"""class Person:
  number_of_people = 0

  def __init__(self,name):
    self.name = name
    Person.add_person()

  @classmethod
  def no_of_people(cls):
    return cls.number_of_people


  @classmethod
  def add_person(cls):
    cls.number_of_people += 1
p1 = Person("tim")
print(p1.number_of_people)
p2 = Person("prajeena")
print(p1.number_of_people)
p3 = Person("twinle")
print(p3.number_of_people)

print(Person.no_of_people())

class Math:
  @staticmethod
  def add5(x):
    return x + 5
  
print(Math.add5(5))"""

class employee:
  def show(self):
    print("i am an employee doing my job")

class teacher(employee):
  def intro(self):
    print("i am a teacher")

class doctor(employee):
  def intro(self):
    print("i am a doctor")

t = teacher()
t.show()
t.intro()