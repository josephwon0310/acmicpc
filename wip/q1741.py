#Connected components?
import sys

input = sys.stdin.readline



#V starts at 1
VE = input()
V, E = map(int, VE.split())
matrix = [[0] * V for _ in range(V)]

for _ in range(E):
    source, to = map(int, input().split())
    matrix[source-1][to-1] = 1
    matrix[to-1][source-1] = 1


    
