input_path = 'input1.txt'
output_path = 'output1.txt'

input_file = open(input_path, 'r')
output_file = open(output_path, 'w')
def printResultToFile(arr):
    for indx in range(len(arr)):
        print(arr[indx], end=" ", file=output_file)
def merge(a, b):
    final_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            final_list.append(a[i])
            i += 1
            continue
        final_list.append(b[j])
        j += 1
    while i < len(a):
        final_list.append(a[i])
        i = i + 1
    while j < len(b):
        final_list.append(b[j])
        j = j + 1

    return final_list
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = merge_sort(arr[0:mid])
        a2 = merge_sort(arr[mid:])
        return merge(a1, a2)
def solve():
    testCase = int(input_file.readline())
    arr = list(map(int, input_file.readline().split(" ")))
    result = merge_sort(arr)
    printResultToFile(result)
solve()
input_file.close()
output_file.close()
