# https://www.acmicpc.net/problem/2121
# 2121
'''
import sys
input = sys.stdin.readline

n=int(input().strip())
a,b = map(int,input().split())
points={}
cnt=0
for i in range(n):
    x,y=map(int,input().strip().split())
    if x not in points.keys(): points[x] = set()
    points[x].add(y)

    for dx,dy in [(x+a,y+b),(x+a,y-b),(x-a,y+b),(x-a,y-b)]:
        if dy in points[x]:
            if dx in points.keys():
                if y in points[dx] and dy in points[dx]:
                    cnt+=1
print(cnt)
'''

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

points = set()
for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))

cnt = 0
for x, y in points:
    if (x + a, y) in points and (x, y + b) in points and (x + a, y + b) in points:
        cnt += 1

print(cnt)
