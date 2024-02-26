
path_input = "input4.txt"
path_output = "output4.txt"
file_input = open(path_input, 'r')
file_output = open(path_output, 'w')
def calculate_max_completed_tasks(arr, person):
    for ind in range(len(arr)):
        min_index = ind
        for j in range(ind + 1, len(arr)):
            if arr[j][1] < arr[min_index][1]:
                min_index = j
        arr[ind], arr[min_index] = arr[min_index], arr[ind]

    count = 1
    person_arr = [0] * person
    person_arr[0] = arr[0][1]

    for i in range(1, len(arr)):
        cur_start, cur_end = arr[i]
        for j in range(person):
            if person_arr[j] <= cur_start:
                person_arr[j] = cur_end
                count += 1
                break

    return count

test_case, person_number = map(int, file_input.readline().split())
data = []
for _ in range(test_case):
    tup = tuple(map(int, file_input.readline().split()))
    data.append(tup)
result = calculate_max_completed_tasks(data, person_number)
file_output.write(str(result) + "\n")
file_input.close()
file_output.close()
