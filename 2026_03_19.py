# https://www.acmicpc.net/problem/23746

n = int(input())
d={}
for i in range(n):
    v,k = input().split()
    d[k] = [v,len(v)]
compressed = input()
s,e = map(int,input().split())
left,right=0,0
i=0
substring=''
while left+d[compressed[i]][1]<s:
    left+=d[compressed[i]][1]
    i+=1
right = left
while right+d[compressed[i]][1]<e:
    substring+=d[compressed[i]][0]
    right+=d[compressed[i]][1]
    i+=1
substring+=d[compressed[i]][0]
print(substring[s-left-1:e-left])