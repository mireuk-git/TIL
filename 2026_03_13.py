# https://www.acmicpc.net/problem/27340

n,m = map(int,input().split())
a = list(map(int,input().split()))

tablecount = 0
color=[]
for i in a:
    if i>=4: color.append(i)
    tablecount += i//4
if n>=m and len(color)==m and tablecount>=n: print("DA")
else: print("NE")