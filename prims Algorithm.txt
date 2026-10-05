# Prim's Algorithm using A, B, C, D

INF = 999999

# Graph using adjacency matrix
graph = [
    [0, 2, 3, 6],   # A
    [2, 0, 1, 4],   # B
    [3, 1, 0, 5],   # C
    [6, 4, 5, 0]    # D
]

vertices = ['A', 'B', 'C', 'D']

selected = [False] * 4
selected[0] = True       # Start from A

total_cost = 0

print("Edges in Minimum Spanning Tree:")

for _ in range(3):
    minimum = INF
    x = 0
    y = 0

    for i in range(4):
        if selected[i]:
            for j in range(4):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(vertices[x], "--", vertices[y], "=", graph[x][y])

    total_cost += graph[x][y]
    selected[y] = True

print("Minimum Cost =", total_cost)