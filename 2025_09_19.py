# https://www.acmicpc.net/problem/26500
# 26500
'''
n=int(input())
for i in range(n):
    a,b=map(float,input().split())
    M,m=max(a,b),min(a,b)
    print(round(M-m,1))
'''
# https://www.acmicpc.net/problem/18795
# 18795

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
trash=sum(a)+sum(b)
print(trash)

