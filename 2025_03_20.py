# https://www.acmicpc.net/problem/17550
# 17550
import sys
n=int(sys.stdin.readline().strip())
l=[]
for _ in range(n): l.append(int(sys.stdin.readline().strip()))

s1,s2=0,sum(l)
m=0

for k in range(n+1):
    if k>0: 
        s1+=l[k-1]**2
        s2-=l[k-1]
    m=max(m,s1*s2)

print(m)

'''
for i in range(n+1):
    s2[i]=total-sum(l[:i])
    
left, right = 0,n
while right-left>2:
    m1=(2*left+right)//3
    m2=(left+2*right)//3
    f1=s1[m1]*s2[m1]
    f2=s1[m2]*s2[m2]

    if f1<f2: left=m1
    else: right=m2

m = max(s1[k]*s2[k] for k in range(left,right+1))
print(m)
'''