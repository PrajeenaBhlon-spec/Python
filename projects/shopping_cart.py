import json
import sys
import time

class cart:
  def __init__(self):
    self.cart = {}

  def add_product(self):
    want_to_add = True
    i = 0
    while want_to_add:
      self.product = input("enter product: ")
      self.size = input("enter size: ")
      self.cart[self.product] = { "size" : self.size}
      ans = input("want to continue? ")
      if ans == "yes":
        want_to_add = True
      else:
        want_to_add = False

      i += 1
    print("Your cart:")
    print(self.cart)
  

  def checkout(self):
    def order_id_generator():
      n = 1
      while True:
        yield f"ORD-{n:04d}"
        n += 1

    with open("projects/products.json" , "r") as file:
      data = json.load(file)
      Total = 0
      print(self.cart)
      for item in self.cart:
        for product in data['products']:
          if product["product"] == item:
            Total += product["price"]

      order_id = order_id_generator()
      print(f"Your order id: {next(order_id)}")
      print(f"Total: {Total}")

class view_product:
  def __init__(self):
    with open("projects/products.json" , "r") as file:
      data = json.load(file)
      self.length = len(data['products'])

    self.start = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    current = self.start
    if current >= self.length:
      raise StopIteration
    self.start += 1
    with open("projects/products.json" , "r") as f:
      data = json.load(f)
      return data['products'][current]
    
c = cart()

while True:

  print("1. View product")
  print("2. Add to cart")
  print("3. Remove from cart")
  print("4. view cart")
  print("5. Checkout")
  print("6. Exit")

  choice = int(input("enter your choice: "))
  if choice == 1:
    product_list = view_product()
    for item in product_list:
      print(item)
 
  elif choice == 2:
    c.add_product()
  
  elif choice == 5:
    c.checkout()
    
  elif choice == 6:
    sys.exit()

