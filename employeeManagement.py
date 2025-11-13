import csv
from pathlib import Path

class employee:
  def __init__(self , name , age , contact ,department):
    self.name = name
    self.age = age
    self.contact = contact
    self.department = department
    file = Path("employee.csv")
    if not file.exists():
      file.touch()
    else:
      with open("employee.csv" , "a" , newline="") as employee_file:
        csv_writer = csv.writer(employee_file , delimiter= ",")
        csv_writer.writerow([self.name,self.age,self.contact,self.department])
      employee_file.close()
  
  def record(self):
    if self.department == "hr" or self.department == "finance":
      with open("employee.csv" , "r" , newline="") as employee_record:
        csv_reader = csv.reader(employee_record)
        next(csv_reader)
        print("List of employee: ")
        for line in csv_reader:
          print(line)
        
      employee_record.close()
    else:
      print("only hr department can view employee records")
    
  def benefits(self):
    if isinstance(self , fulltimeEmployee):
      print("BENEFITS:")
      print("")
      print("1.life insurance ")
      print("2.When there's health issue company will cover")
      print("3.small amount of company share will be given")
    elif isinstance(self , parttimeEmployee):
      print("BENEFITS:")
      print("")
      print("1. paid time off")
      print("2. Flexible hours")
      print("3.remote work options")
    elif isinstance(self , intern):
      print("BENEFITS:")
      print("")
      print("1.mentoship")
      print("2.powerful resume building")


class fulltimeEmployee(employee):
  def __init__(self , name , age , contact , department , post):
    super().__init__( name , age , contact , department)
    self.post = post

  def salary(self):
    if self.department == "software development" and self.post == "front-end developer":
      print("salary: 40k")
    elif self.department == "software development" and self.post == "Back-end developer":
      print("salary: 42k")
    elif self.department == "software development" and self.post == "fullstack developer":
      print("salary: 55k")
    elif self.department == "testing" and self.post == "quality analyst":
      print("salary: 28k")
    elif self.department == "testing" and self.post == "quality tester":
      print("salary: 32k")
    

class parttimeEmployee(employee):
  def __init__(self , name , age , contact  ,department , post):
    super().__init__( name , age , contact , department)
    self.post = post

  def salary(self):
    hour = int(input("how many hour do you work? "))
    salary_paid = 1
    if self.department == "software development" and self.post == "front-end developer":
      salary_paid = hour * 450
      print(f"salary : {salary_paid}")
    elif self.department == "software development" and self.post == "Back-end developer":
      salary_paid = hour * 490
      print(f"salary : {salary_paid}")
    elif self.department == "software development" and self.post == "fullstack developer":
      salary_paid = hour * 530
      print(f"salary : {salary_paid}")
    elif self.department == "testing" and self.post == "quality analyst":
      salary_paid = hour * 300
      print(f"salary : {salary_paid}")
    elif self.department == "testing" and self.post == "quality tester":
      salary_paid = hour * 350
      print(f"salary : {salary_paid}")
    

class intern(employee):
  def __init__(self , name , age , contact ,department , post):
    super().__init__(name , age , contact , department)
    self.post = post

  def salary(self):
    months = int(input("how many months of your internship? "))
    if months > 6:
      if self.department == "software development" and self.post == "front-end developer":
        print("salary: 40k")
      elif self.department == "software development" and self.post == "Back-end developer":
        print("salary: 42k")
      elif self.department == "software development" and self.post == "fullstack developer":
        print("salary: 55k")
      elif self.department == "testing" and self.post == "quality analyst":
        print("salary: 28k")
      elif self.department == "testing" and self.post == "quality tester":
        print("salary: 32k")
      
    else:
      print("you need to exceed 6 months to earn salary")

fte = fulltimeEmployee("prajeena" , 22 , 9825272004 , "software development" , "front-end developer")
fte.salary()

fte.benefits()

pte = parttimeEmployee("kamila" , 25, 9823425611 , "hr" , "hr manager") 
pte.record()