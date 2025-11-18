# https://www.acmicpc.net/problem/12048
# 12048

import sys
input = sys.stdin.readline

t=int(input().strip())
for test_case in range(1,1+t):
    print(f"Case #{test_case}:")
    n,q = map(int,input().strip().split())
    initial = list(map(int,input().strip().split()))

    new = []
    for l in range(n):
        for r in range(l,n):
            new.append(sum(initial[l:r+1]))
    new.sort()

    for i in range(q):
        l,r = map(int,input().strip().split())
        print(sum(new[l-1:r]))