
input_file = "input1b.txt"
output_file = "output1b.txt"
def graph_rep_adj_list(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph[u].append((v, w))
    return graph

def print_graph_adj_list(graph, output_file):
    with open(output_file, 'w') as f:
        for i in range(len(graph)):
            f.write(str(i) + ": ")
            for j in range(len(graph[i])):
                f.write(str(graph[i][j]) + " ")
            f.write("\n")

def main(input_file, output_file):
    graph = graph_rep_adj_list(input_file, output_file)
    print_graph_adj_list(graph, output_file)


main(input_file, output_file)
