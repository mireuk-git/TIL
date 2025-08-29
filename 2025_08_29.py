# https://www.acmicpc.net/problem/21208
# 21208
'''
import sys
input=sys.stdin.readline

n,k=map(int,input().strip().split())
gratFreq={}
for i in range(n*3):
    grat=input().strip()
    if grat in gratFreq.keys():
        gratFreq[grat]+=1
    else:
        gratFreq[grat]=1

for i in range(k):
    m=max(gratFreq.values())
    for j in list(gratFreq.keys())[::-1]:
        if gratFreq[j]==m: 
            print(j)
            gratFreq[j]=-1
            break
'''

import sys
input=sys.stdin.readlines

n=input().splitlines()
print(n)




'''
n,k=map(int,input().strip().split())
gratFreq={}
history={}
for i in range(n*3):
    grat=input().strip()
    gratFreq[grat]=gratFreq.get(grat,0)+1
    history[grat]=i

sortedGrat=sorted(gratFreq.items(),key=lambda x: (x[1],history[x[0]]),reverse=True)

for i in range(min(k,len(sortedGrat))):
    print(sortedGrat[i][0])'''