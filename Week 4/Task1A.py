
input_file = "input1a.txt"
output_file = "output1a.txt"


def graph_rep_adj_matrix(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph[u][v] = w
    return graph

def print_graph_adj_matrix(graph, output_file):
    with open(output_file, 'w') as f:
        for row in graph:
            for val in row:
                f.write(str(val) + " ")
            f.write("\n")

def main(input_file, output_file):
    graph = graph_rep_adj_matrix(input_file, output_file)
    print_graph_adj_matrix(graph, output_file)


main(input_file, output_file)