input_path = 'input2.txt'
output_path = 'output2.txt'

def graphRep(input_file):
    nodes, m = list(map(int, input_file.readline().split(" ")))
    graph = []
    for _ in range(m):
        graph.append(list(map(int, input_file.readline().split(" "))))
    return (nodes, graph)
        
def find(parent, i): 
    if parent[i] != i: 
        parent[i] = find(parent, parent[i]) 
    return parent[i] 


def union(parent, rank, x, y): 
    if rank[x] < rank[y]: 
        parent[x] = y 
    elif rank[x] > rank[y]: 
        parent[y] = x 
    else: 
        parent[y] = x 
        rank[x] += 1

def KruskalMST(nodes, graph, output_file): 
    result = [] 
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2]) 
    parent = [] 
    rank = []

    for node in range(nodes+1): 
        parent.append(node)
        rank.append(0)

    while e < nodes - 1: 
        u, v, w = graph[i] 
        i = i + 1
        x = find(parent, u) 
        y = find(parent, v) 
        if x != y:
            e = e + 1
            result.append([u, v, w]) 
            union(parent, rank, x, y) 

    minimumCost = 0
    for u, v, weight in result: 
        minimumCost += weight  
    output_file.write(str(minimumCost) + "\n") 


with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    n, g = graphRep(input_file)
    KruskalMST(n, g, output_file)
