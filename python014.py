class Difference:
    def __init__(self, a):
        self.maximumDifference = 0
        self.__elements = a

	# Add your code here
    def computeDifference(self):
      min = self.__elements[0]
      max = self.__elements[0]

      for el in self.__elements:
        if(el>max):max = el
        elif(el<min):min = el

      self.maximumDifference = max-min  
      
      return self.maximumDifference
# End of Difference class



# The absolute difference between two integers

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)





# def oddNumbers(l, r):
#     # Write your code here
#     arr = []
#     for el in range (l,r+1):
#       if(el%2!=0):
#            arr.append(el)       

#     return arr


# l=3
# r=9


 
# print(oddNumbers(l, r))