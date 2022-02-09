def shortest_path(edges, node_A, node_B):
  graph = graphBuilder(edges)
  print('graph : ', graph)
  visited = { [ node_A ] }
  queue = [ [ node_A, 0 ] ]
  while( len(queue) > 0 ):
    node, distance = queue.pop(0)

    if node == node_B:
        return distance
    for neighbor in graph[node]:
        if neighbor in visited:
            visited[neighbor] = [ neighbor ] 
            queue.append( [ neighbor, distance + 1 ] )

    return -1
  
def graphBuilder(edges):
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

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'x'))