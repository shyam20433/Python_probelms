graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': [],
    'G': ['L'],
    'H': ['M'],
    'I': ['N', 'O'],
    'J': ['P', 'Q'],
    'K': [],
    'L': ['R'],
    'M': ['R'],
    'N': ['S'],
    'O': ['T'],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': []
}

visited=[]
def dfs(visited,graph,node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
    return '->'.join(visited)


print(dfs(visited,graph,'A'))

'''

def bfs(graph,node):
    visited=[]
    queue=[]
    queue.append(node)
    
    while queue:
        vertex=queue.pop(0)
        visited.append(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    
        
    return visited
'''