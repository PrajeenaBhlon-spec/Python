import json
from datetime import datetime
import sys

now = datetime.now()

class monthly_expense:

  def __init__(self ,name , month_name , food , rent , cloth , education , beauty):
    self.name = name
    self.month_name = month_name
    self.food = food
    self.rent = rent
    self.cloth = cloth
    self.education = education
    self.beauty = beauty

  def enter_expense(self):
    with open("projects/expense.json" , "r") as file:
      data = json.load(file)
      

      new_entry = {}
      total = self.beauty +self.cloth + self.education +self.food + self.rent
      new_entry['name'] = self.name
      new_entry['MONTH'] = self.month_name
      new_entry['food'] = self.food
      new_entry['rent'] = self.rent
      new_entry['cloth'] = self.cloth
      new_entry['education'] = self.education
      new_entry['beauty'] = self.beauty
      new_entry['Total expense'] = total
      data['Expenses'].append(new_entry)
      with open("projects/expense.json" , "w") as f:
        json.dump(data , f , indent= 2)
      
class display_expense:
  def __init__(self):
    with open("projects/expense.json" , "r") as f:
      data = json.load(f)
      self.length = len(data['Expenses'])

    self.start = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    current = self.start
    if current >= self.length:
      raise StopIteration
    self.start += 1
    
    with open("projects/expense.json" , "r") as file:
      data = json.load(file)
      return data['Expenses'][current]

month_name = now.strftime('%B')
option = input("do you want to enter data or view data(view/enter)")
if option == "enter":
  name = input("enter your name: ")
  with open("projects/expense.json" , "r") as f:
    data = json.load(f)
    length = len(data['Expenses'])-1
    for expense in data['Expenses']:
      if expense['name'] == name:
        print("name already exist")
        sys.exit()

  food = int(input(f"enter food expense for {now.strftime('%B')}: "))
  rent = int(input(f"enter rent expense for {now.strftime('%B')}: "))
  cloth = int(input(f"enter cloth expense for {now.strftime('%B')}:"))
  education = int(input(f"enter education expense for {now.strftime('%B')}:"))
  beauty = int(input(f"enter beauty product expense for {now.strftime('%B')}:"))
  e = monthly_expense(name , month_name , food , rent , cloth , education , beauty)
  e.enter_expense()
elif option == "view":
  all_expense = display_expense()
  for item in all_expense:
    print(item)



    



