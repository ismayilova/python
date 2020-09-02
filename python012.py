class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
   def __init__(self,firstName, lastName, idNumber ,scores):
    #   Class Constructor
       Person.__init__(self, firstName, lastName, idNumber)
       self.__scores = scores
   
   def calculate(self):
      sum = 0
      n = len(self.__scores)
      for i in range(0,n):
        sum+= self.__scores[i]

      res  = sum/n
      if res>=90 and res<=100:
        return 'O'
      elif res<90 and res>=80:
        return 'E'
      elif res <80 and res>=70:
        return 'A'
      elif res<70 and res>=55:
        return 'P'
      elif res<55 and res>=40:
        return 'D'
      elif res <40:
        return 'T'        
    

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())