input_path = 'input5.txt'
output_path = 'output5.txt'
input_file = open(input_path, 'r')
output_file = open(output_path, 'w')
def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
def printResultToFile(arr):
    for indx in range(len(arr)):
        print(arr[indx], end=" ", file=output_file)

N = int(input_file.readline())
arr = list(map(int, input_file.readline().split()))

quicksort(arr, 0, N - 1)
printResultToFile(arr)
input_file.close()
output_file.close()
print("Heelllo madafaqin world hfusdgfuisdg") 