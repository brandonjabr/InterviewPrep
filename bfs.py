from Queue import Queue

def reconstruct_path(previous_nodes, start_node, end_node):

    path = []

    # start from the end of the path and work backwards
    curr = end_node

    while curr:
        path.append(curr)
        curr = previous_nodes[curr]

    # reverse our path to get the right order
    path.reverse()  # flip it around, in place
    return path  # no longer reversed

def shortest_path_bfs(graph, start_node, end_node):

    if start_node not in graph:
        raise Exception('Start node not in graph')
    if end_node not in graph:
        raise Exception('End node not in graph')

    to_visit = []
    to_visit.append(start_node)

    visited = {start_node: None}

    while to_visit:
        curr = to_visit.pop(0)

        # stop when we reach the end node
        if curr == end_node:
            return reconstruct_path(visited, start_node, end_node)

        for neighbor in graph[curr]:
            if neighbor not in visited:
                to_visit.append(neighbor)
                visited[neighbor] = curr

    #there's NO path from start_node to end_node
    return None

graph = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2],
}