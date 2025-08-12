# https://www.acmicpc.net/problem/7326
# 7326
'''
n=int(input())
for test_case in range(n):
    x,y=map(int,input().split())
    r="No Number"
    if x==y:
        if x%2==0: r=2*x
        else: r=(x//2)*4+1
    elif x==y+2:
        if x%2==0: r=2*y+2
        else: r=(y//2)*4+3
    print(r)
'''
# https://www.acmicpc.net/problem/17127
# 17127

n=int(input())
a=list(map(int,input().split()))
mp=0
p=[1,1,1,1]
for t1 in range(1,n-2):
    p[0]=1
    for i in range(t1): p[0]*=a[i]
    for t2 in range(t1+1,n-1):
        p[1]=1
        for i in range(t1,t2): p[1]*=a[i]
        for t3 in range(t2+1,n):
            p[2],p[3]=1,1
            for i in range(t2,t3):p[2]*=a[i]
            for i in range(t3,n):p[3]*=a[i]
            if mp<sum(p): mp=sum(p)
print(mp)