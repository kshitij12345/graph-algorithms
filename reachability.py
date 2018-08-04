#Uses python3

import sys


def reach(adj,x,y):
    #write your code here
    global visited
    global reachable
    reachable = False
    visited = [False]*len(adj)
    ret = Explore(x,adj,y)
    if reachable:
        return 1
    return 0

def Explore(v,adj,dest):
    global visited
    global reachable
    visited[v] = True
    #print (adj[v],dest)
    if dest in adj[v]:
        reachable= True
    for neighbour in adj[v]:
        if not visited[neighbour]:
            Explore(neighbour,adj,dest)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print (adj,x,y)
    print(reach(adj, x, y))
