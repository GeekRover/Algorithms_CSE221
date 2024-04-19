import sys
import heapq

input_path = 'input2.txt'
output_path = 'output2.txt'

def graphRepAdjList(input_file):
    (n, m) = tuple(map(int, input_file.readline().split(" ")))
    graph = [[] for i in range(n+1)]
    inDeg = [0]*(n+1)
    for i in range(m):
        (u, v) = tuple(map(int, input_file.readline().split(" ")))
        graph[u].append(v)
        inDeg[v] += 1
    return (graph, inDeg, n)

def bfs(graph, v, visited, result, pQ, inDeg):
    visited.append(v)
    heapq.heappush(pQ,v)
    while pQ:
        x = heapq.heappop(pQ)
        result.append(x)
        for element in graph[x]:
            inDeg[element] -= 1
            if element not in visited and inDeg[element] == 0:
                visited.append(element)
                heapq.heappush(pQ,element)

def topSort(graph, inDeg, node, output_file):
    result = []
    visited = []
    pQ = []
    heapq.heapify(pQ)
    for i in range(1,len(graph)):
        if inDeg[i] == 0 and i not in visited:
            bfs(graph, i, visited, result, pQ, inDeg)

    if len(result) < node:
        output_file.write('IMPOSSIBLE\n')
    else:
        for i in result:
            output_file.write(str(i) + " ")



with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    graph, inDeg, node = graphRepAdjList(input_file)
    topSort(graph, inDeg, node, output_file)
