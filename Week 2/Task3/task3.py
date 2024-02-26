path_input = "input3.txt"
path_output = "output3.txt"
file_input = open(path_input, 'r')
file_output = open(path_output, 'w')
def print_schedule(arr):
    txt = f"{len(arr)}\n"
    for i in arr:
        txt += f"{i[0]} {i[1]}\n"
    return txt

def calculate_max_completed_task(arr):
    new_arr = []
    for ind in range(len(arr)):
        min_index = ind
        for j in range(ind + 1, len(arr)):
            if arr[j][1] < arr[min_index][1]:
                min_index = j
        arr[ind], arr[min_index] = arr[min_index], arr[ind]

    new_arr.append(arr[0])
    prev_start, prev_end = arr[0]
    for i in range(1, len(arr)):
        cur_start, cur_end = arr[i]
        if cur_start >= prev_end:
            new_arr.append(arr[i])
            prev_end = cur_end

    return new_arr

test_case = int(file_input.readline())
data = []
for _ in range(test_case):
    tup = tuple(map(int, file_input.readline().split(" ")))
    data.append(tup)
result = calculate_max_completed_task(data)
file_output.write(print_schedule(result))
file_input.close()
file_output.close()
