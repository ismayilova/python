#!/bin/python3


def findOddEvenLetters(inputStr):
  oddLetters ='';
  evenLetters ='';
  for i  in range(0,len(inputStr)):
    if(i%2==0):
      evenLetters+=inputStr[i]
    else:
      oddLetters += inputStr[i]  
  
  print(f'{evenLetters} {oddLetters}')

if __name__ == '__main__':
    t = int(input())
for i in range(0,t):
  inputStr = input();
  findOddEvenLetters(inputStr)
