#Uses python3

import sys

global dist
global prev

def relax(u,v,cost):
    global dist,prev
    #print (u,v,cost)
    if dist[v]>dist[u]+cost:
        dist[v]=dist[u]+cost
        prev[v]=u
        return True
    return False

def OneIter():
    ret = False
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            v = adj[i][j]
            cos = cost[i][j]
            if relax(i,v,cos):
                ret = True
    return ret

def negative_cycle(adj, cost):
    global dist,prev
    dist = [9999]*len(adj)
    prev = [None]*len(adj)

    dist[0]=0

    #for _ in range(len(adj)):
    #    for i in range(len(adj)):
    #        for j in range(len(adj[i])):
    #           v = adj[i][j]
    #           cos = cost[i][j]
    #           relax(i,v,cos)

    for _ in range(len(adj)):
        OneIter()
    
    #for i in range(len(adj)):
    #    for j in range(len(adj[i])):
    #        v = adj[i][j]
    #        cos = cost[i][j]
    #        if relax(i,v,cos):
    #            return 1

    if OneIter():
        return 1
    
    
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
