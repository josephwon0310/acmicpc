import sys

string = sys.stdin.readline()
d = {}

for i, c in enumerate(string, 0):
    if c not in d.keys():
        d[c] = i


for char in range(97, 123):
    c = chr(char)
    if c in string:
        print(d[c], end=' ')
    else:
        print(-1, end=' ')
