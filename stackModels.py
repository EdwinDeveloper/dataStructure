def depthFirstPrint(graph, source):
    stack = [ source ]
    print("El stack : ", stack)
    while(len(stack) > 0):
        current = stack.pop()
        print(current)

        for neightbor in graph[current]:
            stack.append(neightbor)

def breadFirstPrint(graph, source):
    stack = [ source ]
    print("El stack : ", stack)
    while(len(stack) > 0):
        current = stack.pop(0)
        print(current)

        for neightbor in graph[current]:
            stack.append(neightbor)

graph = {
    'a': ['c','b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f':[]
}

breadFirstPrint(graph, 'a')

