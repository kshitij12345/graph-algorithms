#Uses python3

import sys
global visited
global order
global clock
sys.setrecursionlimit(200000)

def ReverseGraph(adj):
    reverse = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for x in adj[i]:
            reverse[x].append(i)
    return reverse

def dfs(adj):
    global visited
    global order
    global clock
    clock = 1
    visited = [False]*len(adj)
    order = [0]*len(adj)

    for v in range(len(adj)):
        if not visited[v]:
            visited[v]=True
            print (visited)
            for neighbour in adj[v]:
                if not visited[neighbour]:
                    Explore(neighbour,adj)
            order[v]=clock
            clock = clock + 1
    print (order)



def Explore(v,adj):
    global clock
    global visited
    
    visited[v]= True
    for neighbour in adj[v]:
        if not visited[neighbour]:
            Explore(neighbour,adj)
    order[v]=clock
    clock = clock + 1

def ExploreandRemove(v,adj):
    global visited
    global order

    visited[v]= True
    for neighbour in adj[v]:
        if not visited[neighbour]:
            ExploreandRemove(neighbour,adj)
    order[v]=-99
    
def number_of_strongly_connected_components(adj):
    global order
    global visited
    result = 0
    reverse = ReverseGraph(adj)
    dfs(reverse)
    visited = [False]*len(adj)
    while True:
        index = order.index(max(order))
        if max(order) == -99:
            break
        ExploreandRemove(index,adj)
        print(order,visited)
        result = result + 1
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    print(number_of_strongly_connected_components(adj))
