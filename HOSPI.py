from collections import deque

# Hospital floor plan
# S = Patient Room (Start)
# E = Emergency Exit
# . = Empty Path
# # = Wall

hospital = [
    ['S', '.', '.', '#', 'E'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'E', '.']
]

rows = len(hospital)
cols = len(hospital[0])

# Find start position
for i in range(rows):
    for j in range(cols):
        if hospital[i][j] == 'S':
            start = (i, j)

# Four possible movements
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# BFS Queue
queue = deque()
queue.append((start, [start]))

visited = set()
visited.add(start)

while queue:
    (x, y), path = queue.popleft()

    # Exit found
    if hospital[x][y] == 'E':
        print("Shortest Evacuation Path:")
        print(path)
        print("Total Steps =", len(path)-1)
        break

    # Visit neighbouring cells
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if (0 <= nx < rows and
            0 <= ny < cols and
            hospital[nx][ny] != '#' and
            (nx, ny) not in visited):

            visited.add((nx, ny))
            queue.append(((nx, ny), path + [(nx, ny)]))