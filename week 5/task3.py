input_path = 'input3.txt'
output_path = 'output3.txt'

def graphRepAdjList(input_file):
    (n, m) = tuple(map(int, input_file.readline().split(" ")))
    graph = [[] for i in range(n+1)]
    revGraph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input_file.readline().split(" ")))
        graph[u].append(v)
        revGraph[v].append(u)
    return (graph, revGraph)


def dfs(G, v, visited, stack, revTraversal=True, compList = None):
    visited.append(v)
    if not revTraversal:
        compList.append(v)
    for element in G[v]:
        if element not in visited:
            dfs(G, element, visited,stack, revTraversal, compList)
    if revTraversal:
        stack.append(v)


def ssComponent(graph, revGraph, output_file):
    result = []
    visited = []
    stack = []
    for i in range(1,len(graph)):
        if i not in visited:
            dfs(graph, i, visited, stack)

    visited = []
    components = []
    while stack:
        l = []
        x = stack.pop()
        if x not in visited:
            dfs(revGraph,x,visited,stack, revTraversal=False, compList=l)

        if l:
            components.append(l)
        
    for i in components:
        if len(i) > 0:
            for j in i:
                output_file.write(str(j) + " ")
            output_file.write("\n")




with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    graph, revGraph = graphRepAdjList(input_file)
    ssComponent(graph, revGraph, output_file)
