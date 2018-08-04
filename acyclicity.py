#Uses python3

import sys

def acyclic(adj):
    #write your code here
    global Stack
    global visited
    global Cycle
    Cycle = False
    visited = [False]*len(adj)

    for v in range(0,len(adj)):
        Stack = []
        if not visited[v]:
            Stack.append(v)
            visited [v] = True    
            #print (v)
            for neighbour in adj[v]:
                if not visited[neighbour]:
                    Explore(neighbour,adj)
                    #print ("Next non connected")
                    #print (v,visited)
                #print (c)

    #print (max(CCnum))
    if Cycle:
        return 1
    return 0

def Explore(v,adj):
    #print (v)
    global visited
    global Cycle
    global Stack
    Stack.append(v)
    visited[v] = True
    for neighbour in adj[v]:
        if neighbour in Stack:
            Cycle = True
        if not visited[neighbour]:
            #print (neighbour)
            Explore(neighbour,adj)
    Stack.remove(v)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
