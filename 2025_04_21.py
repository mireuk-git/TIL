# https://www.acmicpc.net/problem/24793
# 24793
'''
import sys
input=sys.stdin.readline

n=int(input())
last=input().strip()
l={last}
p=1
prnt="Fair Game"

pin=False

for _ in range(n-1):
    new=input().strip()
    if not pin:
        if (last[-1]!=new[0] or new in l):
            prnt=f"Player {p+1} lost"
        else: 
            p=(p+1)%2
            l.add(new)
            last=new
print(prnt)
'''

# https://www.acmicpc.net/problem/13702
# 13702
import sys

n,k=map(int,input().split())
input=sys.stdin.readline
l=[]
for _ in range(n):
    l.append(int(input()))
    