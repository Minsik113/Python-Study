import sys

n = int(sys.stdin.readline())
ans = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ans.append([a, b])

ans.sort(key=lambda x:(x[0], x[1]))

for i in ans:
    print(f'{i[0]} {i[1]}')