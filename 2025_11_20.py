# https://www.acmicpc.net/problem/13229
# 13229

import sys
input=sys.stdin.readline

n = int(input().strip())
l = list(map(int,input().strip().split()))
m = int(input().strip())
for _ in range(m):
    start,end = map(int,input().strip().split())
    s = sum(l[start:end+1])
    print(s)