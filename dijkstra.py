#Uses python3

import sys
import queue

def distance(adj, cost, s, t):
    processed = [False]*len(adj)
    dist = [9999]*len(adj)
    prev = [None]*len(adj)
    Q = queue.PriorityQueue()
    dist[s]=0
    for node in range(len(adj)):
        Q.put((dist[node],node))
        
    while not Q.empty():
        u = Q.get()
        u = u[1]
        if processed[u]:
            continue
        processed[u]=True
        for i in range(len(adj[u])):
            v = adj[u][i]
            #print (dist)
            if dist[v]>(dist[u]+cost[u][i]):
                dist[v]=dist[u]+cost[u][i]
                prev[v]=u
                #print(dist[v],v)
                Q.put((dist[v],v))
    if dist[t]!=9999:
        return dist[t]
    
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    #print(cost)
    #print(adj)
    print(distance(adj, cost, s, t))
