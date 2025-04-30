# https://www.acmicpc.net/problem/29718
# 29718

import sys

input=sys.stdin.readline
n,m=map(int,input().strip().split())
row_count=[0]*m
for _ in range(n):
    l=list(map(int,input().split()))
    for i in range(len(l)): row_count[i]+=l[i]

a=int(input())
max_claps=0
for i in range(m-a+1):
    count=0
    for j in range(i,i+a):
        count+=row_count[j]
    if count>max_claps:
        max_claps=count

print(max_claps)