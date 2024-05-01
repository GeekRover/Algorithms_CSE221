
input_path = 'input3.txt'
output_path = 'output3.txt'

def climb_stairs(n):
    if n <= 1:
        return n
    f = [0] * (n+1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    n = int(input_file.readline())
    result = climb_stairs(n)
    output_file.write(str(result) + "\n")
