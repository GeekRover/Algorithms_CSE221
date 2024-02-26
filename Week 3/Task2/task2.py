input_path = 'input2.txt'
output_path = 'output2.txt'
input_file = open(input_path, 'r')
output_file = open(output_path, 'w')
def findMax(left, right):
    if left > right:
        return left
    else:
        return right

def divideAndFindMax(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left = divideAndFindMax(arr[:mid])
    right = divideAndFindMax(arr[mid:])
    return findMax(left, right)

def printResultToFile(result):
    print(result, file=output_file)

def solve():
    testCase = int(input_file.readline())
    arr = list(map(int, input_file.readline().split(" ")))
    result = divideAndFindMax(arr)
    printResultToFile(result)

solve()

input_file.close()
output_file.close()
