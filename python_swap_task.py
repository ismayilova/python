#!/bin/python3

import math
import os
import random
import re
import sys


# 
#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
def reverse_words_order_and_swap_cases(sentence):
  
  res  = ''
  arr = []
  swaped = sentence.swapcase()
  s = swaped.split()
  n = len(s)
 
  print(s)
  for i in range(0,n,1):
    res+=(s[n-i-1]+' ')
    arr.append(s[n-i-1])
  print(arr) 
  return res


    

   

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
