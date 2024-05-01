input_path = 'input1.txt'
output_path = 'output1.txt'


def find(parent, node):
    while parent[node] != node:
        node = parent[node]
    return parent[node]

def printSetNodes(parent, node):
    count = 0
    for i in parent:
        if i == node:
            count += 1
    return count

def union(parent, node1, node2):
    node1Parent = find(parent, node1)
    node2Parent = find(parent, node2)
    for i in range(1,len(parent)):
        if parent[i] == node2Parent:
            parent[i] = node1Parent
    return printSetNodes(parent, node1Parent)

def disjoint(nodes, connection, input_file, output_file):
    parent = []
    for i in range(nodes+1):
        parent.append(i)
    for i in range(connection):
        node1, node2 = list(map(int, input_file.readline().split(" ")))
        result = union(parent, node1, node2)
        output_file.write(str(result) + "\n")


with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    nodes, connection = list(map(int, input_file.readline().split(" ")))
    disjoint(nodes, connection, input_file, output_file)
