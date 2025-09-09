def func(amt):
  print(amt)
def add(a,b):
  c=a+b
  func(c)
add(3,5)

amount =10
def func(amt):
  print(amt)
func(amount)

import math
amount =10.4
def func(amt):
  amt=math.floor(amt)
  print(amt)
  amt=10.5
  amt=math.ceil(amt)
  print(amt)
func(amount)

try:
  c=5/0
  print(c)
except ZeroDivisionError:
  print("code not working call")
