import sys

#string = sys.stdin.readline()
string = input()
d = {}

for c in string:
    #if ord(c) >= 97 and ord(c) < 123:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

print(d)
