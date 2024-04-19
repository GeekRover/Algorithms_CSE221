from heapq import heappop, heappush
input_path = 'input3.txt'
output_path = 'output3.txt'
def graphRepAdjList(input_file):
    (n, m) = tuple(map(int, input_file.readline().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v, w) = tuple(map(int, input_file.readline().split(" ")))
        graph[u].append((v,w))
    return graph

def find_safest_path(graph, source, destination):
    distance = [float('inf') for node in range(len(graph))]

    distance[source] = 0
    minHeap = [(0, source)]

    while minHeap:
        curDist, curNode = heappop(minHeap)
        if curDist > distance[curNode]:
            continue

        for element, weight in graph[curNode]:
            new_distance = max(curDist, weight)
            if new_distance < distance[element]:
                distance[element] = new_distance
                heappush(minHeap, (new_distance, element))

    if distance[destination] == float('inf'):
        return "Impossible"
    return distance[destination]



with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    graph = graphRepAdjList(input_file)
    safest_path_distance = find_safest_path(graph, 1, len(graph)-1)
    output_file.write(str(safest_path_distance) + "\n")
