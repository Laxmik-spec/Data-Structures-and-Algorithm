
# ** Breadth First Search
# This code implements the Breadth-First Search (BFS) algorithm for traversing a graph

import collections
def bfs(graph, start):
    visited = set()
    queue = collections.deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("Breadth-First Search starting from vertex A:")
    bfs(graph, 'A')