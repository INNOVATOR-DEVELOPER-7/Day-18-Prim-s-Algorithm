# Day-18-Prim-s-Algorithm
Here' s Python program for Prim's Algorithm. Day 18 of Day 365.
- Initial Setup: Start with a weighted, connected, and undirected graph, represented as nodes (vertices) and edges with weights. Choose a starting node (source) and initialize a priority queue.
- Priority Queue Initialization: Insert the starting node into the priority queue with a distance of zero, and all other nodes with a distance of infinity.
- Minimum Spanning Tree (MST) Set: Create an MST set to keep track of the nodes included in the MST.
- Explore Nodes:
  - Extract the node with the smallest distance (let's call it the current node) from the priority queue.
  - Add the current node to the MST set.
  - For each neighbor of the current node:
    - If the neighbor is not in the MST set and the weight of the edge (current node, neighbor) is less than the known distance, update the distance.
    - If the distance is updated, add or update the neighbor in the priority queue with the new distance.
- Repeat: Continue the process until all nodes are included in the MST set.

Example:
Graph:

```
    (2)       (3)
  A ----- B ------ C
    \    |      /
  (6)\   |     /(5)
      \   |   /
       v  v  /
        D -- E
       (4)
```

Starting Node: A

1. Initial Priority Queue: [(A, 0), (B, ∞), (C, ∞), (D, ∞), (E, ∞)]
2. Extract A, update distances:
   - Distance to B: 2
   - Distance to D: 6
   - Updated Priority Queue: [(B, 2), (D, 6), (C, ∞), (E, ∞)]
   - MST Set: [A]
3. Extract B, update distances:
   - Distance to C: 3
   - Distance to E: 5
   - Updated Priority Queue: [(C, 3), (E, 5), (D, 6)]
   - MST Set: [A, B]
4. Extract C, update distances:
   - Distance to E: 5 (already smaller)
   - Updated Priority Queue: [(E, 5), (D, 6)]
   - MST Set: [A, B, C]
5. Extract E, update distances:
   - Distance to D: 4
   - Updated Priority Queue: [(D, 4)]
   - MST Set: [A, B, C, E]
6. Extract D, no further updates.
   - Final MST Set: [A, B, C, E, D]

Edges in MST:
- (A, B) with weight 2
- (B, C) with weight 3
- (E, D) with weight 4
- (B, E) with weight 5

The Minimum Spanning Tree includes the edges (A, B), (B, C), (E, D), and (B, E) with a total weight of 14.
