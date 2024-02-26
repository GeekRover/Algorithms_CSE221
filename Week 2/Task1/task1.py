# o(a^2)
file1 = open("input1.txt", "r")
input = file1.readlines()
lst = input[1].split()
inp = input[0].split()
a = int(inp[0])
b = int(inp[1])
txt = ""
output = None
for i in range(a):
  lst[i] = int(lst[i])
for i in range(a):
  for j in range(i+1, a):
    if lst[i] + lst[j] == b:
      output = f"{i+1} {j+1}"
      break
if output == None:
  output = "IMPOSSIBLE"
txt += output
print(output)
file2 = open("output1.txt", "w" )
file2.writelines(txt)
file2.close()


# o(a)
file1 = open("input1.txt", "r")
input_lines = file1.readlines()
lst = input_lines[1].split()
inp = input_lines[0].split()
a = int(inp[0])
b = int(inp[1])
txt = ""
output = None
lst = [int(x) for x in lst]
left_pointer = 0
right_pointer = a - 1
while left_pointer < right_pointer:
    current_sum = lst[left_pointer] + lst[right_pointer]
    if current_sum == b:
        output = f"{left_pointer + 1} {right_pointer + 1}"
        break
    elif current_sum < b:
        left_pointer += 1
    else:
        right_pointer -= 1
if output is None:
    output = "IMPOSSIBLE"
txt += output
print(output)
file2 = open("output1.txt", "w")
file2.writelines(txt)
file2.close()
