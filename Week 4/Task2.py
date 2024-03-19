
input_file = "input2.txt"
output_file = "output2.txt"
def graph_rep_adj_list(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph[v].append(u)
    return graph

def bfs(graph, source, output_file):
    visited = [-1] * len(graph)
    queue = []
    sequence = str(source)
    queue.append(source)
    while queue:
        s = queue.pop(0)
        adj = graph[s]
        for element in adj:
            if visited[element] == -1:
                visited[element] = 0
                sequence += " " + str(element)
                queue.append(element)
        visited[s] = 1
    with open(output_file, 'w') as f:
        f.write(sequence + "\n")

def main(input_file, output_file):
    graph = graph_rep_adj_list(input_file, output_file)
    bfs(graph, 1, output_file)


main(input_file, output_file)
