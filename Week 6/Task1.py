input_path = 'input1.txt'
output_path = 'output1.txt'

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) < 2:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_value

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent][1] > self.heap[index][1]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        min_index = index
        if left_child < len(self.heap) and self.heap[left_child][1] < self.heap[min_index][1]:
            min_index = left_child
        if right_child < len(self.heap) and self.heap[right_child][1] < self.heap[min_index][1]:
            min_index = right_child
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._bubble_down(min_index)

    def get_min(self):
        return self.heap[0]


def graphRepAdjList(input_file):
    (n, m) = tuple(map(int, input_file.readline().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v, w) = tuple(map(int, input_file.readline().split(" ")))
        graph[u].append((v,w))
    source = int(input_file.readline())
    return (graph, source)

def dijkstra(graph, source):
    heap = MinHeap()
    dist = [float('inf') for i in range(len(graph))]
    parent = [-1 for i in range(len(graph))]

    dist[source] = 0
    parent[source] = 0
    heap.insert((source, 0))
    while len(heap.heap) != 0:
        ver, weight = heap.remove()
        for element, eleWeight in graph[ver]:
            if dist[element] > dist[ver] + eleWeight:
                dist[element] = dist[ver] + eleWeight
                parent[element] = ver
                heap.insert((element, eleWeight))
    
    return dist



with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    g, s = graphRepAdjList(input_file)
    distance = dijkstra(g, s)

    for i in range(1, len(distance)):
        if distance[i] == float('inf'):
            output_file.write('-1 ')
        else:
            output_file.write(str(distance[i]) + " ")
