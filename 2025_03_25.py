# https://www.acmicpc.net/problem/8989
# 8989
t=int(input())
for _ in range(t):
    l=list(input().split())
    k=[]
    for i in range(len(l)):
        k.append(list(map(int,l[i].split(":"))))
        k[i][0]=(k[i][0]%12)*5+k[i][1]/12
        k[i]=(abs(k[i][0]-k[i][1]))
        k[i]=min(k[i],60-k[i])
    z=sorted(zip(k,l),key=lambda x:(x[0],int(x[1][0:2])*60+int(x[1][3:])))
    k,l=zip(*z)
    print(l[len(l)//2])

