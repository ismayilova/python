
import math
import os
import random
import re
import sys

def reverseArray(arr):
  
  n = len(arr)
  str1  = ''
  for i in range(0 ,n):
    
    str1+=str(arr[n-i-1])+' '

  
  return str1




if __name__ == '__main__':
   


  # txt = "welcome to the jungle"
  # y = txt.split()
  # x = txt.rstrip().split()

  # print(x)   
  # print(y)
   
   n = int(input())
   arr = list(map(int, input().rstrip().split()))
   print(arr)
   print(reverseArray(arr))