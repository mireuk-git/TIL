# https://www.acmicpc.net/problem/32385
# 32385

n=int(input())
a=[]

if n%2:
    k=(n-3)//2
    for i in range(1,k+1):
        a.append(i)
        a.append(-i)
    a+=[-(k+1),-(k+2),2*k+3]
else:
    for i in range(1,n//2+1):
        a.append(i)
        a.append(-i)

a.append(0)

for i in a:
    print(i,end=' ')