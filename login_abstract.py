from abc import ABC , abstractmethod
import json

class verify_login(ABC):
  @abstractmethod
  def user_login_verify(self , username , password):
    pass

  @abstractmethod
  def admin_login_verify(self , admin_name , admin_password):
    pass

class login(verify_login):

  def user_login_verify(self, username, password):
    self.username = username
    self.password = password
    with open("login.json" , "r") as f:
      user_data = json.load(f)
      
      for user in user_data["users"]:
        if self.username == user['username'] and self.password == user['password']:
          found = True
          print("User verfication complete")
          print("login successfull")
          break
      
      if not found:
        print("invalid user credentials")
    f.close()
    
  
  def admin_login_verify(self, admin_name, admin_password):
    self.admin_name = admin_name
    self.admin_password = admin_password
    with open("login.json" , "r") as f:
      admin_data = json.load(f)
      found = None
      for user in admin_data["admin"]:
        if self.admin_name == user['admin name'] and self.admin_password == user['admin password']:
          found = True
          print("admin verfication complete")
          print("login successfull")
          break
      
      if not found:
        print("invalid admin credentials")
    f.close()



identity = input("are you user or admin: ")
if identity == "user":
  user = login()
  name = input("enter username: ")
  pws = input("enter you password: ")
  user.user_login_verify(name , pws)
else:
  admin = login()
  adminname = input("enter admin name: ")
  adminpws = input("enter admin password: ")
  admin.admin_login_verify(adminname , adminpws)