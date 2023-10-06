graph = {
    "A": [("B", 5), ("F", 11)],
    "B": [("C", 1), ("E", 5), ("F", 3)],
    "C": [("D", 2), ("E", 4)],
    "D": [("G", 2)],
    "E": [("D", 9),("G", 1)],
    "F": [("E", 2), ("H", 9)],
    "G": [],
    "H": []
}

start_state = "A" # starting state of the bfs
goal_state = "G" # the destination/goal of the bfs


def find_all_paths(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return [path]

    if start not in graph:
        return []

    all_paths = []

    for neighbor, _ in graph[start]:
        if neighbor not in path:
            new_paths = find_all_paths(graph, neighbor, goal, path)
            for new_path in new_paths:
                all_paths.append(new_path)

    return all_paths

all_paths = find_all_paths(graph, start_state, goal_state)

if all_paths:
    print(f"All paths from {start_state} to {goal_state}:")
    for path in all_paths:
        print(" -> ".join(path))

print(f"\ntraversed path from {start_state} to {goal_state}:")

def bfs_paths(graph, start, goal):
    visited = set()
    queue = [] # list for visited nodes (fringe)
    parent = {} # close nodes

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ") #traversed nodes

        if node == goal:
            path = []
            while node is not None:
                path.insert(0, node)
                node = parent.get(node)
            return path

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    return None

shortest_path = bfs_paths(graph, start_state, goal_state)
print(f"\nShortest path:\n{shortest_path}")

