input_path = 'input4.txt'
output_path = 'output4.txt'

input_file = open(input_path, 'r')
output_file = open(output_path, 'w')

def merge(arr, left, mid, right):
    arr1 = arr[left:mid]
    arr2 = arr[mid:right + 1]
    i = 0
    j = 0
    k = left
    maxVal = float('-inf')

    while i < len(arr1) and j < len(arr2):
        if arr1[i] + arr2[j] ** 2 > maxVal:
            maxVal = arr1[i] + arr2[j] ** 2
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    return maxVal
def mergeSort(arr, left, right):
    maxVal = float('-inf')
    if left < right:
        mid = (left + right) // 2
        maxVal = max(maxVal, mergeSort(arr, left, mid))
        maxVal = max(maxVal, mergeSort(arr, mid + 1, right))
        maxVal = max(maxVal, merge(arr, left, mid, right))
    return maxVal
def printResultToFile(result):
    print(result, file=output_file)

l = int(input_file.readline())
arr = list(map(int, input_file.readline().split(" ")))

maxVal = mergeSort(arr, 0, len(arr)-1)
printResultToFile(maxVal)

input_file.close()
output_file.close()
