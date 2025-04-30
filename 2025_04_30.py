# https://www.acmicpc.net/problem/13915
# 13915
'''
import sys

input=sys.stdin.readline
while True:
    n=input().strip()
    if not n: break
    n=int(n)
    s=set()
    for _ in range(n):
        t=set(input().strip())
        t=''.join(sorted(t))
        s.add(t)
    print(len(s))
'''
# https://www.acmicpc.net/problem/1269
# 1369

n,m=map(int,input().split())
a=set(list(input().split()))
b=set(list(input().split()))

r=len(a-b)
r+=len(b-a)
print(r)