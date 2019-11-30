import sys, operator

word = sys.stdin.readline
d = {}
for char in input():
    char = char.upper()
    if char in d.keys():
        d[char] += 1
    else:
        d[char] = 1

if len(d) > 1:
    a = max(d.items(), key=operator.itemgetter(1))[0]
    aval = d[a]
    del d[a]
    b = max(d.items(), key=operator.itemgetter(1))[0]

    if aval > d[b]:
        print(a)
    else:
        print('?')

else:
    print(max(d.items(), key=operator.itemgetter(1))[0])
