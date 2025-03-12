# https://www.acmicpc.net/problem/9086
# 9086
'''
t=int(input())
for i in range(t):
    s=input()
    print(s[0]+s[-1])
'''

# https://www.acmicpc.net/problem/26595
# 26595
'''
def treesearch(n,p,c,x=0,y=0):
    a,b=0,0
    if n>=p[0]:
        xa,ya=treesearch(n-p[0],p,c,x+1,y)
        a=c[0]*xa+c[1]*ya
    if n>=p[1]:
        xb,yb=treesearch(n-p[1],p,c,x,y+1)
        b=c[0]*xb+c[1]*yb
    if a>b: x,y=xa,ya
    elif b>a: x,y=xb,yb
    return x,y

n=int(input())
c=[0,0]
p=[0,0]
c[0],p[0],c[1],p[1]=map(int,input().split())

x,y=treesearch(n,p,c)
print(x,y)
'''

n=int(input())
a,pa,b,pb=map(int,input().split())
X,Y,m=0,0,0
for x in range(n//pa,-1,-1):
    y=(n-pa*x)//pb
    p=a*x+b*y
    if p>m: X,Y,m=x,y,p
print(X,Y)



