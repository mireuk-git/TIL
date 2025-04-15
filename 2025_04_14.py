# https://www.acmicpc.net/problem/9012
# 9012
'''
n=int(input())
for _ in range(n):
    s=input()
    count=0
    for c in s:
        if c=="(": count+=1
        elif c==")": count-=1
        if count<0:break
    if count==0: print("YES")
    else: print("NO")
'''
# https://www.acmicpc.net/problem/24653
# 24653

n=int(input())
s=list(map(int,input().split()))
t=int(input())

cnt=set()
for i in s:
    cnt.add(i//t)
print(len(cnt))