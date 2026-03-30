# https://www.acmicpc.net/problem/15161

k=int(input())
mat=[[k+1 for j in range(10)] for i in range(10)]
for w in range(1,k+1):
    l = list(map(int,input().split()))
    for i in range(3):
        for j in range(10):
            mat[l[i]-1][j]=k+1-w
    for i in range(3):
        for j in range(10):
            mat[j][l[i+3]-1]=k+1-w
for i in mat:
    for j in i:
        print(j,end=" ")
    print()