# ** Depth First Search
# This code implements the Depth-First Search (DFS) algorithm for traversing a graph

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)
    return visited

graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3']),
}
print("Depth-First Search starting from vertex 0:")
dfs(graph, '0')
print()


