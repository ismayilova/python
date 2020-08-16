#!/bin/python3

import math
import os
import random
import re
import sys
# Определите, существует ли непустая строка, которая встречается как подстрока и в , и в .
# Complete the twoStrings function below.
def twoStrings(s1, s2):
  sets1 = set(s1)
  sets2 = set(s2)
  res  = ''
  if sets1.isdisjoint(sets2):
    res = 'NO'
  else:
     res = 'YES' 

  return res 


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
