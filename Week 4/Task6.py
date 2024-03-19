input_file = "input6.txt"
output_file = "output6.txt"

def bfs(graph, r, h, visited):
    row, col = len(graph), len(graph[0])
    diamonds = 0
    Q = [(r, h)]
    visited[r][h] = True
    while Q:
        x, y = Q.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and graph[nx][ny] != '#':
                if graph[nx][ny] == 'D':
                    diamonds += 1
                visited[nx][ny] = True
                Q.append((nx, ny))
    return diamonds, visited

def find_max_diamond(graph, row, col):
    max_diamonds = 0
    visited = [[False] * col for _ in range(row)]

    for r in range(row):
        for h in range(col):
            if graph[r][h] == '.':
                d, visited = bfs(graph, r, h, visited)
                max_diamonds = max(max_diamonds, d)
    return max_diamonds

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        row, col = map(int, f.readline().split())
        graph = [f.readline().strip() for _ in range(row)]
    result = find_max_diamond(graph, row, col)
    with open(output_file, 'w') as f:
        f.write(str(result) + '\n')



main(input_file, output_file)
