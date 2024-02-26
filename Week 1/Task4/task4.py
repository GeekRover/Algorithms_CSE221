# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WNtme8YwTFvUDxvdiDbNtSwGUbae3Vl0
"""

input_path = "/content/drive/MyDrive/CSE221inputs/Lab1/Task4/input4.txt"
input = open(input_path, "r")
lst = input.readlines()
f_int = int(lst[0])
input = lst[1:]
txt = ""
train_lst = []
place_lst = []
departure_lst = []
for i in range(len(input)):
    temp_lst = input[i].split()
    a,b,c,d,e,f,g = tuple(temp_lst)
    train_lst.append(a)
    place_lst.append(e)
    departure_lst.append(g)
time_lst = []
for i in range(f_int):
    sum = 0
    lst = departure_lst[i].split(":")
    x,y = lst
    sum = int(x)*100 + int(y)
    time_lst.append(sum)
for i in range(f_int):
    for j in range(0, f_int-i-1):
        if train_lst[j] > train_lst[j+1]:
            train_lst[j], train_lst[j+1] = train_lst[j+1], train_lst[j]
            place_lst[j], place_lst[j+1] = place_lst[j+1], place_lst[j]
            departure_lst[j], departure_lst[j+1] = departure_lst[j+1], departure_lst[j]
            time_lst[j], time_lst[j+1] = time_lst[j+1], time_lst[j]
        elif train_lst[j] == train_lst[j+1]:
            if time_lst[j] < time_lst[j+1]:
                place_lst[j], place_lst[j+1] = place_lst[j+1], place_lst[j]
                departure_lst[j], departure_lst[j+1] = departure_lst[j+1], departure_lst[j]
                time_lst[j], time_lst[j+1] = time_lst[j+1], time_lst[j]
for i in range(f_int):
    output = f'{train_lst[i]} will departure_lst for {place_lst[i]} at {departure_lst[i]}\n'
    txt += output
output_path = "/content/drive/MyDrive/CSE221inputs/Lab1/Task4/output4.txt"
output = open(output_path, "w")
output.writelines(txt)
output.close()