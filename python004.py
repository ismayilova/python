class Person:

  def __init__(self, initialAge):
    if initialAge<0:
        self.initialAge = 0
        print('Age is not valid, setting age to 0.')
    else:
      self.initialAge = initialAge

  def yearPasses(self):
      self.initialAge+=1

  def amIOld(self):
    if self.initialAge<13:
      print('You are young.')
    elif 13<=self.initialAge<18:
      print('You are a teenager.')
    else:
      print('You are old.ArithmeticError')    





t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
    print(p.initialAge)

