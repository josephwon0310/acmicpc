import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
directions = [
    (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)
]


def traverse(matrix, i, j):
    global x, y
    if matrix[i][j] == 0:
        return

    matrix[i][j] = 0

    for d in directions:
        ny = i + d[0]
        nx = j + d[1]
        if nx < 0 or ny < 0 or nx >= x or ny >= y:
            continue
        if matrix[ny][nx] == 1:
            traverse(matrix, ny, nx)


def countIsland(x, y, matrix):
    cnt = 0
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == 1:  # island
                cnt += 1
                traverse(matrix, i, j) #matrix, y, x
    return cnt


while True:
    xandy = input()
    if len(xandy) < 3:
        break
    global x, y
    x, y = map(int, xandy.split())

    matrix = [list(map(int, input().split())) for _ in range(y)]
    print(countIsland(x, y, matrix))
