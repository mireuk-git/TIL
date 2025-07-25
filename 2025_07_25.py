# https://www.acmicpc.net/problem/25562
# 25562

n=int(input())

print(n*(n-1)//2)
t=1
for i in range(1,n+1):
    print(t,end=' ')
    t*=2
print()

print(n-1)
for i in range(1,n+1):
    print(i,end=' ')