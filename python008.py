
import math
import os
import random
import re
import sys





if __name__ == '__main__':
   
  n = int(input())  #numbers of data to add in phoneBooks
  phoneBooks= {}
  for i in range(0,n):
    str1 = input().rstrip().split()
    phoneBooks[str1[0].rstrip()] = str1[1]
 
  for line in sys.stdin:
    # print(line, end='')
    key = str(line).rstrip()
    res = phoneBooks.get(f'{key}')
    
    if res ==None:
      print('Not found')
    else:
      print(f'{key}={res}')  

  

