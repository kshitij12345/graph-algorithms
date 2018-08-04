#Uses python3

import sys
import queue

def bipartite(adj):
    s = 0
    q = queue.Queue()
    dist = [9999]*len(adj)
    prev = [None]*len(adj)
    dist[s]=0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v]==9999:
                q.put(v)
                dist[v]=dist[u]+1
                prev[v]=u

    for i in range(len(adj)):
        for neighbour in adj[i]:
            if dist[i]==dist[neighbour]:
                return 0
    
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
