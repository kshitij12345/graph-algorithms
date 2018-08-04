#Uses python3

import sys
global Clock
global used
global order
Clock = 1

def Explore(adj,v):
    global Clock
    global used
    global order
    used[v] = True
    #print (adj[v],dest)
    for neighbour in adj[v]:
        if not used[neighbour]:
            Explore(adj,neighbour)
    order[v]=Clock
    Clock = Clock + 1
    

def dfs(adj):
    global Clock
    global used
    global order
    for x in range(len(adj)):
        #print (used)
        if not used[x]:
            used[x]=True
            for neighbour in adj[x]:
                if not used[neighbour]:
                    Explore(adj,neighbour)
            order[x] = Clock
            Clock = Clock + 1
    


def toposort(adj):
    global used
    global order
    used = [False] * len(adj)
    order = [0]*len(adj)
    dfs(adj)
    print (order)
    o = []
    for i in range(len(order)):
        index = order.index(max(order))
        o.append(index)
        order[index]=-99
    order = [x for x in o]
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print (adj)
    order = toposort(adj)
    
    for x in order:
        print(x + 1, end=' ')

