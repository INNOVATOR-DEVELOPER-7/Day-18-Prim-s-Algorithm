import heapq

def prim(graph, start_node):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = [(0, start_node)]
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        
        visited[u] = True
        mst_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))

    return mst_cost, mst_edges

# Get the number of vertices from the user
num_vertices = int(input("Enter the number of vertices: "))

# Initialize the graph as an adjacency list
graph = [[] for _ in range(num_vertices)]
print("Enter each edge in the format 'u v weight' (0-based index):")
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# Get the starting node from the user
start_node = int(input("Enter the starting node (0-based index): "))

# Perform Prim's algorithm
mst_cost, mst_edges = prim(graph, start_node)

# Print the result
print("Minimum Spanning Tree cost:", mst_cost)
print("Edges in the Minimum Spanning Tree:")
for u, v, w in mst_edges:
    print(f"({u}, {v}) with weight {w}")
