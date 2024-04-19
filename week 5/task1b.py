input_path = 'input1b.txt'
output_path = 'output1b.txt'

def graphRepAdjList(input_file):
    (n, m) = tuple(map(int, input_file.readline().split(" ")))
    graph = [[] for i in range(n+1)]
    inDeg = [0]*(n+1)
    for i in range(m):
        (u, v) = tuple(map(int, input_file.readline().split(" ")))
        graph[u].append(v)
        inDeg[v] += 1
    return (graph, inDeg, n)

def bfs(G, v, visited, result, Q, inDeg):
    visited.append(v)
    Q.append(v)
    while Q:
        x = Q.pop(0)
        result.append(x)
        for adj in G[x]:
            inDeg[adj] -= 1
            if adj not in visited and inDeg[adj] == 0:
                visited.append(adj)
                Q.append(adj)

def topSort(graph, inDeg, node, output_file):
    result = []
    visited = []
    Q = []
    for i in range(1, len(graph)):
        if inDeg[i] == 0 and i not in visited:
            bfs(graph, i, visited, result, Q, inDeg)

    if len(result) < node:
        output_file.write('IMPOSSIBLE\n')
    else:
        for i in result:
            output_file.write(str(i) + " ")



with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    graph, inDeg, node = graphRepAdjList(input_file)
    topSort(graph, inDeg, node, output_file)
