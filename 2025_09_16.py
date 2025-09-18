# https://www.acmicpc.net/problem/32714
# 32714

n=int(input())
t=3*n-4
if n==2:
    t=1
elif n==3:
    t=3
print(t)