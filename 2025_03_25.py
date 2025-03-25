# https://www.acmicpc.net/problem/8989
# 8989
t=int(input())
for _ in range(t):
    l=list(input().split())
    k=[[]]*len(l)
    for i in range(len(l)):
        k[i]=list(map(int,l[i].split(":")))
        k[i][0]=(k[i][0]%12+k[i][1]/60)*5
        k.append(abs(k[i][0]-k[i][1]))
    z=sorted(zip(l,k))
    l,k=zip(*z)
    print(l[len(l)//2])

