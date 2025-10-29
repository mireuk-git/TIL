# https://www.acmicpc.net/problem/1769
# 1769

x=input()
cnt=1
next_x=0
for i in x:
    next_x+=int(i)
if len(x)==1: cnt-=1
x=next_x

while x>9:
    next_x = 0
    while x>0:
        next_x+=x%10
        x//=10
    x=next_x
    cnt+=1
print(cnt)
if x%3==0: print("YES")
else: print("NO")