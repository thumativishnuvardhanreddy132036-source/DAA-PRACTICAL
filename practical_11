
# Floyd-Warshall Algorithm with User Input

INF = float('inf')

n = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix:")
print("Enter 0 if there is no edge (except on the diagonal).")

graph = []

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    graph.append(row)

# Convert 0 (no edge) to infinity, except on the diagonal
for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] == 0:
            graph[i][j] = INF

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(
                graph[i][j],
                graph[i][k] + graph[k][j]
            )

# Display shortest distance matrix
print("\nAll-Pairs Shortest Distance Matrix:")
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("INF", end="\t")
        else:
            print(int(graph[i][j]), end="\t")
    print()