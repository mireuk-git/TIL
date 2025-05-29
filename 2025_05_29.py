# https://www.acmicpc.net/problem/23909
# 23909
'''
import sys
input=sys.stdin.readline

t=int(input().strip())
for case_num in range(1,t+1):
    n=int(input().strip())
    v=list(map(int,input().strip().split()))
    c=0
    max_left=0
    for i in range(n):
        if v[i]>max_left and (i==n-1 or v[i]>v[i+1]):
            c+=1
        max_left=max(v[i],max_left)
    print(f"Case #{case_num}:",c)
'''
import sys
input=sys.stdin.readline

t=int(input().strip())
for case_num in range(1,t+1):
    n=int(input().strip())
    v=list(map(int,input().strip().split()))
    
    c=0
    max_left=-1

    for i in range(n):
        if v[i]>max_left and (i==n-1 or v[i]>v[i+1]):
            c+=1
        max_left=max(max_left, v[i])
    print(f"Case #{case_num}:",c)