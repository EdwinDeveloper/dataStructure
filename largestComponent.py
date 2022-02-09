graph = {
    '0' : ['8','1','5'],
    '1' : ['0'],
    '5' : ['0','8'],
    '8' : ['0','5'],
    '2' : ['3','4'],
    '3' : ['2','4'],
    '4' : ['3','2']
}

def exproreSize(graph, node, visited):
    if node in visited:
        return 0
    
    visited[node] = []

    size = 1

    for neighbor in graph[node]:
        explore = exproreSize(graph, neighbor, visited)
        size = size + explore
        print(size)

    return size

def largest_component(graph):
    visited = {}
    longest = 0
    for node in graph:
        size = exproreSize(graph, node, visited)
        if size > longest:
            longest = size
    return longest

print('final : ',largest_component(graph))
