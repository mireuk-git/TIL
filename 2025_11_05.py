# https://www.acmicpc.net/problem/6147
# 6147

import sys
input=sys.stdin.readline

n,b = map(int,input().strip().split())
h=[]
for i in range(n): h.append(int(input().strip()))
h.sort(reverse=True)

s=0
for cnt in range(n):
    s+=h[cnt]
    if s >= b:
        break
cnt+=1
print(cnt)