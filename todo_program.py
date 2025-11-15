import json

class todo_class:

  def __init__(self , name):
    self.name = name

  def create_task_field(self):

    key_name = self.name + "_" + "task"
    with open("todo.json" , "r") as f:
      data = json.load(f)
    f.close()

    with open("todo.json" , "w") as f:
      data[key_name] = []
      
      json.dump(data , f , indent= 2)
    f.close()


  def add_list(self):
    key_name = self.name + "_" + "task"
    task_name = input("Task: ")
    task_status = input("Status: ")
    new_entry = {}
    with open("todo.json" , "r") as f:
      data = json.load(f)
    
    with open("todo.json" , "w") as f:
      new_entry["task name"] = task_name
      new_entry["task status"] = task_status
      data[key_name].append(new_entry)
     
      json.dump(data , f , indent= 2)


name = input("enter name: ")
s = todo_class(name)
ques = input("do you already have a key in there?(ex:yourname_task) ")
if ques == "yes":
  pass
else:
  s.create_task_field()

status = input("Want to add tasks?(yes/no) ")
while status != "no":
  s.add_list()
  status = input("Want to keep on adding tasks?(yes/no) ")
