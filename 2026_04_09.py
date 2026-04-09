# https://www.acmicpc.net/problem/14551

n,m = map(int,input().split())
a=1
for i in range(n):
    a*=max(1,int(input()))
    a%=m
a%=m
print(a)