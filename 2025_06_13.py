# https://www.acmicpc.net/problem/22952
# 22952

n=int(input())
a=[]
for i in range(1,n//2+1):
    a.append(n+1-i)
    a.append(i)
if n%2:
    a.append(n//2+1)
for i in a:
    print(i,end=' ')