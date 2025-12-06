students = [
  {"name":"prajeena" , "age":30 , "address": "padampokhari"},
  {"name":"aayush" , "age":23 , "address":"sanupokhara"},
  {"name":"pramila" , "age": 20 , "address":"piple"}
]
sorted_by_age = sorted(students , key=lambda student : student["age"])
print(sorted_by_age)



list_of_num = [4 , 7 , 8 , 48 , 5 , 1]
even_num = list(filter(lambda x : x % 2 == 0 , list_of_num))
print(even_num)


number = [1 , 3 , 5 , 6 , 8]
cube = list(map(lambda x : x*x*x , number))
print(cube)

max = lambda a , b: a if a > b else b
print(f"max number: {max(7 , 20)}")