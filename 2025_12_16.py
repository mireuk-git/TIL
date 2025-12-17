# https://www.acmicpc.net/problem/12755
# 12755

n=int(input())
d=1
c=9
start=1
while n > d*c:
    n-=d*c
    d+=1
    c*=10
    start*=10

t=(n-1)//d
s=str(start+t)
print(s[(n-1)%d])

