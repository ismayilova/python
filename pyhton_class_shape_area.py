#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    
  def __init__(self, a, b ):
    self.a =a 
    self.b = b

  def area(self):
    return round(self.a*self.b,2)  
class Circle:
    

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    s=(self.radius**2)* math.pi
    return round(s, 2)


    
if __name__ == '__main__':
  r = Rectangle(4,5.00)
  print(r.area())
  c= Circle(3)
  print(c.area())