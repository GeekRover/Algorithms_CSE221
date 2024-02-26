file1 = open("input2.txt", "r")
input_lines = file1.readlines()
m = int(input_lines[0])
n = int(input_lines[2])
lst1 = input_lines[1].split()
lst2 = input_lines[3].split()
def merge_sort(lst):
  if len(lst) <= 1:
    return lst

  mid = len(lst) // 2
  left_half = lst[:mid]
  right_half = lst[mid:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)

def merge(lst1, lst2):
  result = []
  i = 0
  j = 0
  while i < len(lst1) and j < len(lst2):
    if lst1[i] <= lst2[j]:
      result.append(lst1[i])
      i += 1
    else:
      result.append(lst2[j])
      j += 1

  result.extend(lst1[i:])
  result.extend(lst2[j:])
  return result

for i in range(m):
  lst1[i] = int(lst1[i])
for i in range(n):
  lst2[i] = int(lst2[i])

lst1 = merge_sort(lst1)
lst2 = merge_sort(lst2)

output = merge(lst1, lst2)
txt = " ".join(map(str, output))
file2 = open("output2.txt", "w")
file2.writelines(txt)
file2.close()


#O(N) approach
def merge(list_1, list_2):
  merged_list = []
  i = j = 0

  while i < len(list_1) and j < len(list_2):
    if list_1[i] <= list_2[j]:
      merged_list.append(list_1[i])
      i += 1
    else:
      merged_list.append(list_2[j])
      j += 1
  merged_list.extend(list_1[i:])
  merged_list.extend(list_2[j:])
  return merged_list
def sorting(list_1, list_2):
  merged_list = merge(list_1, list_2)
  return merged_list
list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 8]
sortedList = sorting(list_1, list_2)
print(sortedList)
