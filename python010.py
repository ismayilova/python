
import math
import os
import random
import re
import sys

def countInteger(n):
  k=0  #sequence counter
  n=0
  for i in range(0,len(b)):
   
    if(int(b[i])==1):
      
      k=k+1  #count integeres 1111 -4      
          #count at least 1 integer
       
    else:
      k =0
    
    if( k>n):
      n=k

       
       

  return n



if __name__ == '__main__':
   
  n = int(input())  
 

  b = ''
 
  while n > 0:
    b = str(n % 2) + b
    n = n // 2

  #print(b)
  print(countInteger(b))

