# https://www.acmicpc.net/problem/17206
# 17206
'''
t=int(input())
l=list(map(int,input().split()))
for _ in range(t):
    sum=0
    s=set()
    for i in range(3,l[_]+1,3): s.add(i)
    for i in range(7,l[_]+1,7): s.add(i)
    for i in s: sum+=i
    print(sum)
'''
'''
t=int(input())
l=list(map(int,input().split()))
for _ in range(t):
    sum3=(l[_]//3+1)*3*(l[_]//3)//2
    sum7=(l[_]//7+1)*7*(l[_]//7)//2
    sum21=(l[_]//21+1)*21*(l[_]//21)//2
    print(sum3+sum7-sum21)
'''