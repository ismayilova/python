git import math
import os
import random
import re
import sys
# Complete the gameOfThrones function below.
def gameOfThrones(s):
 keys = set(s)
 res = 'YES'
 bad_n = 0
 for i in keys:
  n=s.count(i) #count of the letter 
  if n%2!=0:
    bad_n+=1

  if bad_n>1:
   res = 'NO' 
 
 return res  
 
#   pol_dict[i]=s.count(i)
#  print(pol_dict)




s = input()

result =gameOfThrones(s) 
print(result)
print('END')

