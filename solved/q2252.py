import sys

######main######
q = []
d = {}

#num of vertices, num of edges
n, m = map(int, input().split())

#indegree array
in_degree = [0 for _ in range(n+1)]

for line in sys.stdin:
    front, behind = map(int, line.split())
    in_degree[behind] += 1
    if front in d.keys():
        d[front].add(behind)
    else:
        s = set()
        d[front] = s
        d[front].add(behind)

for i in range(1,n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    node = q.pop(0)
    print(node, end=' ')
    if node in d:
        for adj in d[node]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                q.append(adj)

