#Uses python3

import sys


def reach(adj,x,y):
    #write your code here
    global visited
    global CCnum

    visited = [False]*len(adj)
    CCnum = [0]*len(adj)
    
    c =1
    for v in range(0,len(adj)):
        if not visited[v]:
            visited [v] = True    
            CCnum[v] = c
            #print (v)
            for neighbour in adj[v]:
                if not visited[neighbour]:
                    Explore(neighbour,adj,c)
                    #print ("Next non connected")
                    #print (visited)
                    c+=1
                #print (c)

    #print (max(CCnum))
    if CCnum[x]==CCnum[y]:
        return 1
    return 0

def Explore(v,adj,c):
    #print (v)
    global visited
    global CCnum
    #print (visited)
    visited[v] = True
    CCnum[v] = c
    for neighbour in adj[v]:
        if not visited[neighbour]:
            Explore(neighbour,adj,c)


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
    print(reach(adj, x, y))
