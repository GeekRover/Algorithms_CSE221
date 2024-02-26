input_path = 'input6.txt'
output_path = 'output6.txt'
input_file = open(input_path, 'r')
output_file = open(output_path, 'w')
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def findKthSmallest(arr, low, high, k):
    if k > 0 and k <= high - low + 1:
        pi = partition(arr, low, high)
        if pi - low == k - 1:
            return arr[pi]
        if pi - low > k - 1:
            return findKthSmallest(arr, low, pi - 1, k)
        return findKthSmallest(arr, pi + 1, high, k - pi + low - 1)

l = int(input_file.readline())
arr = list(map(int, input_file.readline().split()))
cases = int(input_file.readline())

for i in range(cases):
    result = findKthSmallest(arr, 0, l - 1, int(input_file.readline()))
    print(result, file=output_file)

input_file.close()
output_file.close()
