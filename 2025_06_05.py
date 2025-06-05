# https://www.acmicpc.net/problem/14723
# 14723

n=int(input())
a,b,s=1,1,1
while s<n:
    b+=1
    s+=b
for i in range(s,n,-1):
    a+=1
    b-=1
print(a,b)
