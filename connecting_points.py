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
        return self.label

def cost(x,y):
    return ((x[0]-x[1])**2 +(y[0]-y[1])**2)**0.5

def minimum_distance(x, y):
    Q = PriorityQueue()
    result = 0.
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
            result = result + q[0]


            
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
