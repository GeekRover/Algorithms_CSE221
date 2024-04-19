input_path = 'input1a.txt'
output_path = 'output1a.txt'

def graphRepAdjList(input_file):
    (n, m) = tuple(map(int, input_file.readline().split(" ")))
    graph = [[] for i in range(n+1)]
    inDeg = [0]*(n+1)
    for i in range(m):
        (u, v) = tuple(map(int, input_file.readline().split(" ")))
        graph[u].append(v)
        inDeg[v] += 1
    return (graph, inDeg, n)

def dfs(G, v, visited, inDeg, result):
    visited.append(v)
    result.append(v)
    for element in G[v]:
        inDeg[element] -= 1
        if element not in visited and inDeg[element] == 0:
            dfs(G, element, visited, inDeg, result)

def topSort(graph, inDeg, node, output_file):
    result = []
    visited = []
    for i in range(1, len(graph)):
        if inDeg[i] == 0 and i not in visited:
            dfs(graph, i, visited, inDeg, result)
    if len(result) < node:
        output_file.write('IMPOSSIBLE\n')
    else:
        for i in result:
            output_file.write(str(i) + " ")



with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    graph, inDeg, node = graphRepAdjList(input_file)
    topSort(graph, inDeg, node, output_file)
