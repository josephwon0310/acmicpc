import sys

def DFS(G, vertex):
    stack = []
    stack.append(vertex)

    while stack:
        v = stack.pop()
        if v in vertices:
            vertices.remove(v)
        
        for adj in G[v]:
            if adj in vertices:
                stack.append(adj)


######main######
n, m = map(int, input().split()) #num v and num e

vertices = set()
for v in range(1, n+1):
    vertices.add(v)

G = {}
for i in range(1, n+1):
    G[i] = []

cc = 0 #counter for connected components

#construct graph
for line in sys.stdin:
    u, v = map(int, line.split())
    G[u].append(v)
    G[v].append(u)

#count cc
while vertices:
    root = vertices.pop()
    DFS(G, root)
    cc += 1

print(cc)
        

