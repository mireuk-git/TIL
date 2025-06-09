# https://www.acmicpc.net/problem/1676
# 1676
'''
n=int(input())
m=1
for i in range(2,n+1):
    m*=i
d=10
i=0
while m%d==0:
    d*=10
    i+=1
print(i)
'''
'''
n=int(input())
quin=5
deci=0
while quin<=n:
    deci+=n//quin
    quin*=5
print(deci)
'''

# https://www.acmicpc.net/problem/3211
# 3211

n=int(input())
z=[int(input()) for _ in range(n)]
z.sort()
for i in range(len(z)):
    if z[i]==i: break
print(i+1)
