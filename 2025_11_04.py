# https://www.acmicpc.net/problem/10041
# 10041

w,h,n=map(int,input().split())
x1,y1=map(int,input().split())
cnt=0
for i in range(n-1):
    flag=True
    x2,y2 = map(int,input().split())
    if x2<x1:
        x1,x2=x2,x1
        y1,y2=y2,y1
        flag=False
    if y2<y1:
        cnt+=abs(x2-x1)+abs(y1-y2)
    else:
        cnt += max(abs(x2-x1),abs(y2-y1))
    if flag: x1,y1=x2,y2
print(cnt)
