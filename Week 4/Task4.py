input_file = "input4.txt"
output_file = "output4.txt"

def graph_rep_adj_list(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
    return graph

def check_cycle_util(graph, source, visited, in_stack):
    if in_stack[source] == 1:
        return True
    if visited[source] == 1:
        return False
    visited[source] = 1
    in_stack[source] = 1
    for v in graph[source]:
        if check_cycle_util(graph, v, visited, in_stack):
            return True
    in_stack[source] = -1
    return False

def check_cycle(graph):
    visited = [-1] * len(graph)
    in_stack = [0] * len(graph)
    for source in range(len(graph)):
        if check_cycle_util(graph, source, visited, in_stack):
            return True
    return False

def main(input_file, output_file):
    graph = graph_rep_adj_list(input_file, output_file)
    with open(output_file, 'w') as f:
        if check_cycle(graph):
            f.write("YES\n")
        else:
            f.write("NO\n")



main(input_file, output_file)
