# Expense Tracker 

This project stores monthly expense on basic things like food , rent , education , cloth , beauty product using JSON. Modules like datetime , json and sys are used to write this program. It is a simple project shwocasing the use of iterator .

# How the project works

* First the program asks if user wants to enter or view data.
* if user chooses "view" as an option then display_expense class is called to iter through the stored data inside expense.json . Here the display_expense is an iterator class with dunder methods such as __init__, __iter__, __next__
* if user chooses "enter" as an option then the user is asked to enter their name first . If that name already exists in the json then a message is printed saying "name already exists" .Otherwise , expenses on basic things for the specific month needs to be entered.
* Then an instance of class monthly_expense is created . Data is also sent at the same time in order to be initialized by __init__ method. The object is then used to call enter_expense() method which then stores the data inside json using json module.

## How to run the game

1. Make sure you have python installed
2. Save the script as Expense_tracker.py
3. Run it using:
   python Expense_tracker.py


# Output

### when view option
![Alt Text]()

### when enter option is choosed
 