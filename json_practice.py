import json
import time

def add_student():
  
  with open("csit_8th.json" , "r") as f:
    new_entry = {}
    data = json.load(f)
    ans = input("do you want to enter new student?(yes/no)")
    
    while ans != "no":
      name = input("enter name")
      phn = input("enter phone")
      adr = input("enter address")
      new_entry['name'] = name
      new_entry['phone'] = phn
      new_entry['address'] = adr
      
      with open("csit_8th.json" , "w") as file:
        data['students'].append(new_entry)
        json.dump(data , file , indent= 2)
      file.close()
      time.sleep(2)
      ans = input("do you want to enter new student?(yes/no)")

def view_data():
  with open("csit_8th.json") as file:
    stu_data = json.load(file)
    for data in stu_data['students']:
      print(data)

def add_teacher():
  with open("csit_8th.json" , "r") as file:
    data = json.load(file)

  
  with open("csit_8th.json" , "w") as f:
    data['teachers'] = [
      {
        "name" : "durga",
        "subject" : "java"
      },
      {
        "name" : "sonam",
        "subject" : "spm"
      }
    ]
    json.dump(data , f , indent = 2)




view_data()
add_student()
add_teacher()

