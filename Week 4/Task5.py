input_file = "input5.txt"
output_file = "output5.txt"

def graph_rep_adj_list(input_file):
    with open(input_file, 'r') as f:
        n, m, d = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph[v].append(u)
    return graph, d

def bfs(graph, source, parent, distance):
    q = []
    distance[source] = 0
    q.append(source)

    while q:
        source = q.pop(0)
        for element in graph[source]:
            if distance[element] == float('inf'):
                parent[element] = source
                distance[element] = distance[source] + 1
                q.append(element)

def find_short_distance(graph, source, destination):
    parent = [-1] * len(graph)
    distance = [float('inf')] * len(graph)
    bfs(graph, source, parent, distance)

    if distance[destination] == float('inf'):
        return "Source and Destination are not connected"

    output = ["Time: " + str(distance[destination]) + "\n"]
    path = []
    cur_node = destination
    path.append(destination)
    while parent[cur_node] != -1:
        path.append(parent[cur_node])
        cur_node = parent[cur_node]
    path_str = "Shortest Path: "
    for i in range(len(path) - 1, -1, -1):
        path_str += str(path[i]) + " "
    output.append(path_str + "\n")

    return output

def main(input_file, output_file):
    graph, destination = graph_rep_adj_list(input_file)
    output = find_short_distance(graph, 1, destination)
    with open(output_file, 'w') as f:
        f.writelines(output)



main(input_file, output_file)
