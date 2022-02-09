edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
    ['z', 'i'],
    ['y', 'z']
]

def buildGraph(edges):
    """
    Builder function graph
    """
    graph = {}

    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def hasPath(graph, nodeA, nodeB, visited):
    if nodeA == nodeB: return True
    if nodeA in visited: return False

    visited[nodeA] = []
    for neighbor in graph[nodeA]:
        if hasPath(graph, neighbor, nodeB, visited) == True:
            return True
    return False

def undirectPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, {})

print(undirectPath(edges, 'i', 'z'))
