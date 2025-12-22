# https://www.acmicpc.net/problem/31497
# 31497

import sys
input = sys.stdin.readline

n = int(input().strip())
names = []
for i in range(n):
    names.append(input().strip())

lie=0
for i in range(n):
    res=[]
    for j in range(2):
        print("?",names[i],flush=True)
        res.append(int(input().strip()))
    s = sum(res)
    if s==1:
        lie=i+1
    elif s>1:
        print("!",names[i],flush=True)
        lie=False
        break
if lie:
    print("!",names[lie-1],flush=True)