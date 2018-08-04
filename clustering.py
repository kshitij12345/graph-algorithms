#Uses python3
import sys
import math
from queue import PriorityQueue



"""
MakeSet(x) initializes disjoint set for object x
Find(x) returns representative object of the set containing x
Union(x,y) makes two sets containing x and y respectively into one set

Some Applications:
- Kruskal's algorithm for finding minimal spanning trees
- Finding connected components in graphs
- Finding connected components in images (binary)
"""

def MakeSet(x):
     x.parent = x
     x.rank   = 0

def Union(x, y):
     xRoot = Find(x)
     yRoot = Find(y)
     if xRoot.rank > yRoot.rank:
         yRoot.parent = xRoot
     elif xRoot.rank < yRoot.rank:
         xRoot.parent = yRoot
     elif xRoot != yRoot: # Unless x and y are already in same set, merge them
         yRoot.parent = xRoot
         xRoot.rank = xRoot.rank + 1

def Find(x):
     if x.parent == x:
        return x
     else:
        x.parent = Find(x.parent)
        return x.parent

""""""""""""""""""""""""""""""""""""""""""

import itertools

class Vertex:
    def __init__ (self, label):
        self.label = label
        self.parent = None
        self.rank = None
    def __str__(self):
        return str(self.label)

def cost(x,y):
    return ((x[0]-x[1])**2 +(y[0]-y[1])**2)**0.5

def clustering(x, y, k):
    Q = PriorityQueue()
    result = 0.
    cnt = len(x)-k+1
    le = len(x)
    #print(cnt)
    a = []
    b = []
    for i in range(len(x)): 
        for j in range(i+1,len(x)):
            a.append(x[i])
            a.append(x[j])
            b.append(y[i])
            b.append(y[j])
            c = cost(a,b)
            #print ("cost",c)
            Q.put((c,[i,j]))
            a = []
            b = []

    l = [Vertex(ch) for ch in range(len(x))]
    [MakeSet(i) for i in l]

    while not Q.empty():
        q = Q.get()
        x = q[1][0]
        y = q[1][1]
        if Find(l[x]) != Find(l[y]):
            Union(l[x],l[y])
            cnt = cnt-1
            #s = ""
            #for i in range(le):
            #    s = s + str(Find(l[i]))+ " "
            #print (s)
            #print (q)
            if cnt ==0:
                break
            result = result + q[0]

    #s = ""
    #for i in range(le):
    #    s = s + str(Find(l[i]))+ " "
    #print (s)
    #print(Q.get())
      
    return q[0]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]

    #x = [7,4,5,1,2,5,3,7,2,4,6,2]
    #y = [6,3,1,7,7,7,3,8,8,4,7,6]
    #k = 3

    #x = [3,1,4,9,9,8,3,4]
    #y = [1,2,6,8,9,9,11,12]
    #k = 4
    print("{0:.9f}".format(clustering(x, y, k)))
