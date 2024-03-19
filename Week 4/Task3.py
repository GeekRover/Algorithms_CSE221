input_file = "input3.txt"
output_file = "output3.txt"
def graph_rep_adj_list(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph[v].append(u)
    return graph

def dfs(graph, source, output_file):
    visited = [-1] * len(graph)
    sequence = ""
    visited[source] = 0
    visited, sequence = dfs_visit(graph, source, visited, sequence)
    with open(output_file, 'w') as f:
        f.write(sequence + "\n")

def dfs_visit(graph, u, visited, sequence):
    visited[u] = 1
    sequence += str(u) + " "
    for element in graph[u]:
        if visited[element] == -1:
            visited, sequence = dfs_visit(graph, element, visited, sequence)
    return visited, sequence

def main(input_file, output_file):
    graph = graph_rep_adj_list(input_file, output_file)
    dfs(graph, 1, output_file)



main(input_file, output_file)
