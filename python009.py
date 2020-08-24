
import math
import os
import random
import re
import sys

def factorial(n):
  if n==1:
    return 1
  elif n>1:
    return n*factorial(n-1)



if __name__ == '__main__':
   
  n = int(input())  #numbers of data to add in phoneBooks
  print(factorial(n))

