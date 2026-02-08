class Calcolator:

  num =100

  def __init__(self,a,b):
    self.first = a 
    self.second  = b
    print("this is from class side")

  def getdata(self):
    print("hello from function inside class")

  def wellcominMsg(self):
    print("hello from parant   class")


  def summition(self,a,b):
    self.first + self.second
    return

obj = Calcolator(10,10)

print(obj.getdata())

  
