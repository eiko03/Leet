graph = {
            'a':[ 'c', 'b',],
            'b':['d'],
            'c':['e'],
            'd':['f'],
            'e':[],
            'f':[]
        }
        
        
def dfs(graph, source):
    stack = [source]
    while len(stack) > 0:
        poped = stack.pop()
        print(poped)
        for nodes in graph[poped]:
            stack.append(nodes)
            
def bfs(graph, source):
    stack = [source]
    while len(stack) > 0:
        poped = stack.pop(0)
        print(poped)
        for nodes in graph[poped]:
            stack.append(nodes)
    
def dfs_rec(graph, source):
    print(source)
    for node in graph[source]:
        dfs_rec(graph, node)
    
        
dfs(graph , 'a')
bfs(graph , 'a')
dfs_rec(graph , 'a')
