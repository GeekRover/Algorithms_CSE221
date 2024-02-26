input_path = 'input3.txt'
output_path = 'output3.txt'

input_file = open(input_path, 'r')
output_file = open(output_path, 'w')

def merge(arr, temp, l, mid, r):
    i = k = l
    j = mid + 1
    count = 0

    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1

    for x in range(l, r + 1):
        arr[x] = temp[x]

    return count
def mergeSort(arr, temp, l, r):
    count = 0

    if l < r:
        mid = (l + r) // 2
        count += mergeSort(arr, temp, l, mid)
        count += mergeSort(arr, temp, mid + 1, r)
        count += merge(arr, temp, l, mid, r)

    return count
def printResultToFile(result):
    print(result, file=output_file)
n = int(input_file.readline())
arr = list(map(int, input_file.readline().split()))

temp = [0] * n
result = mergeSort(arr, temp, 0, n - 1)
printResultToFile(result)

input_file.close()
output_file.close()
