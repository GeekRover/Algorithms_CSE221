# -*- coding: utf-8 -*-
"""Lab1_Task1B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VrYe2YqTzBCBjCXo9u7Ccq6qx3swazwp
"""

location = "/content/drive/MyDrive/CSE221inputs/Lab1/Task1/input1b.txt"
input = open(location, "r")
test_cases = input.readline()
lst = input.readlines()
txt = ""
for i in lst[0:int(test_cases)]:
  split = i.split()
  if split[2] == "+":
    txt = txt + f"The result of {split[1]} {split[2]} {split[3]} is {int(split[1]) + int(split[3])}" + "\n"
  elif split[2] == "-":
    txt = txt + f"The result of {split[1]} {split[2]} {split[3]} is {int(split[1]) - int(split[3])}"  + "\n"
  elif split[2] == "/":
    txt = txt + f"The result of {split[1]} {split[2]} {split[3]} is {int(split[1]) / int(split[3])}"  + "\n"
  else:
    txt = txt + f"The result of {split[1]} {split[2]} {split[3]} is {int(split[1]) * int(split[3])}"  + "\n"
location1 = "/content/drive/MyDrive/CSE221inputs/Lab1/Task1/output1b.txt "
output = open(location1, "w")
output.writelines(txt)
output.close()