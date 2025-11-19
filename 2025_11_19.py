# https://www.acmicpc.net/problem/11576
# 11576

a,b=map(int,input().split())
m=int(input())
l=list(map(int,input().split()))

s=0
for i in l:
    s*=a
    s+=i

r=[]
while s>0:
    r.append(s%b)
    s//=b

r_str = ''
r.reverse()
for i in r:
    r_str+=str(i)+" "
print(r_str)