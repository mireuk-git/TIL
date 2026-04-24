# https://www.acmicpc.net/problem/15923

n=int(input())
point = []
for i in range(n):
    point.append(tuple(map(int,input().split())))
l=0
for i in range(n-1):
    if point[i][0]==point[i+1][0]: l+=abs(point[i][1]-point[i+1][1])
    elif point[i][1]==point[i+1][1]: l+=abs(point[i][0]-point[i+1][0])
if point[-1][0]==point[0][0]: l+=abs(point[-1][1]-point[0][1])
elif point[-1][1]==point[0][1]: l+=abs(point[-1][0]-point[0][0])
print(l)
