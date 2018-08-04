#Uses python3

import sys
import queue
global prev

def bfs(adj, s):
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
    #print (dist)
    return [x for x in range(len(dist)) if dist[x]!=9999]

def relax(u,v,cost):
    global distance,prev
    #print (u,v,cost)
    if distance[v]>distance[u]+cost:
        distance[v]=distance[u]+cost
        prev[v]=u
        return v

def OneIter():
    changed = []
    ret = False
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            v = adj[i][j]
            cos = cost[i][j]
            r = relax(i,v,cos)
            if r:
                changed.append(r)
    return changed
    
    
def shortet_paths(adj, cost, s, distance, reachable, shortest):
    global prev
    prev = [None]*len(adj)

    distance[s]=0
    for _ in range(len(adj)):
        OneIter()


    bfslist = OneIter()
        
    for i in range(len(distance)):
        if distance[i]!=10**19:
            reachable[i]=1
            shortest[i]=1
    
    for i in bfslist:
        l = bfs(adj,i)
        for x in l:
            reachable[x]=1
            shortest[x]=0



if __name__ == '__main__':
    global distance,reachable,shortest
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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

