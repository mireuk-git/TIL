# https://www.acmicpc.net/problem/14394
# 14394

c=input()
goal=input()
l=[0]*4
l2=[0]*4

for _ in range(10):
    if c[_] == "R": l[0]+=1
    elif c[_] == "Y": l[1]+=1
    elif c[_] == "B": l[2]+=1
    elif c[_] == "G": l[3]+=1

    if goal[_] == "R": l2[0]+=1
    elif goal[_] == "Y": l2[1]+=1
    elif goal[_] == "B": l2[2]+=1
    elif goal[_] == "G": l2[3]+=1

r=0
for i in range(4):
    if l[i]>l2[i]:
        r+=l[i]-l2[i]
print(r)