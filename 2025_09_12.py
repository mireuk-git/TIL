# https://www.acmicpc.net/problem/18703
# 18703

import sys
input=sys.stdin.readline

t=int(input().strip())
for test_case in range(1,1+t):
    n=int(input().strip())
    original={}
    for i in range(n):
        name,id=input().strip().split()
        id=int(id)
        if name in original.keys():
            if original[name]>id:
                original[name]=id
        else: original[name]=id
    l=[]
    for i in original.keys():
        l.append(original[i])
    l.sort()
    for i in l:
        print(i,end=' ')
    print()
