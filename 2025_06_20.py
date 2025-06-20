# https://www.acmicpc.net/problem/14717
# 14717

a,b=map(int,input().split())
total=9*17
ans=0
if a==b:
    ans=total-(10-a)
else:
    ggeut=(a+b)%10
    for x in range(1,11):
        for y in range(x+1,11):
            if (x+y)%10<ggeut: 
                if x in (a,b) or y in (a,b):
                    ans+=2
                else: ans+=4
print("%.3f"%(ans/total))