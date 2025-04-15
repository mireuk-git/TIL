# https://www.acmicpc.net/problem/8989
# 8989
'''
t=int(input())
for _ in range(t):
    times=list(input().split())
    angles=[]
    for time in times:
        h,m=map(int,time.split(":"))
        angle=abs((h%12)*30-5.5*m)
        angles.append(min(angle,360-angle))
    z=sorted(zip(angles,times))
    angles,times=zip(*z)
    print(times[2])
'''
# https://www.acmicpc.net/problem/2168
# 2168

from math import gcd
x,y=map(int,input().split())
print(x+y-gcd(x,y))