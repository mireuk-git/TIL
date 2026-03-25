# https://www.acmicpc.net/problem/16677

m=input()
n=int(input())
l=[]
for i in range(n):
    w,g=input().split()
    index=0
    for c in w:
        if index==len(m): break
        if c==m[index]: index+=1
    if index==len(m):
        if len(w)==len(m): continue
        g = int(g)/(len(w)-len(m))
        l.append((w,g,i))

if len(l)==0: print("No Jam")
else:
    l.sort(key=lambda x: (-x[1],x[2]))
    print(l[0][0])