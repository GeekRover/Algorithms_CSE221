import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    inDeg = [0]*(n+1)
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        inDeg[v] +=1
    print(graph, inDeg)
    return (graph, inDeg, n)

def dfs(G, v, visited, inDeg, result):
    visited.append(v)
    result.append(v)
    for element in G[v]:
        inDeg[element] -= 1
        if element not in visited and inDeg[element] == 0:
            dfs(G, element, visited, inDeg, result)


def topSort(graph, inDeg, node):
    result = []
    visited = []
    for i in range(1,len(graph)):
        if inDeg[i] == 0 and i not in visited:
            dfs(graph, i, visited, inDeg, result)
    print(result)
    if len(result) < node:
        print('IMPOSSIBLE')
    else:
        for i in result:
            print(i, end=" ")

def main():
    sys.stdin = open('input1a.txt', 'r')
    sys.stdout = open('output1a.txt', 'w')
    graph, inDeg, node = graphRepAdjList()
    topSort(graph, inDeg, node)

if __name__ == "__main__":
    main()