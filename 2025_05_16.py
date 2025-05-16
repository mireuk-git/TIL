# https://www.acmicpc.net/problem/11739
# 11739

n,k=map(int,input().split())
p=[]
for _ in range(n):
    p.append(list(map(int,input().split())))

l=0
a=0
j_max=max([p[i][0] for i in range(n)])
i,j=0,1

while a<k:
    if p[i][0]>=j:
        if p[i][j]>=l:
            l+=p[i][j]
            a+=1
    else: 
        l+=50
        a+=1
    i=(i+1)%n
    if not i: j+=1

if a<k:
    l+=(k-a)*50

print(l)