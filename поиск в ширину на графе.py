graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
#node - это узел
visited = [] #списока посещённых вершин
queue = [] #вершины в очереди на посещение

def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end='')
        for neighbor in graph[s]:
           if neighbor not in visited:
               visited.append(neighbor)
               queue.append(neighbor)

bfs(visited, graph, 'A')
