# 11109
# https://www.acmicpc.net/problem/11109

t=int(input())
for test_case in range(t):
    d,n,s,p=map(int,input().split())
    t1 = d+p*n
    t2 = n*s
    if t1 < t2: print("parallelize")
    elif t1 > t2: print("do not parallelize")
    else: print("does not matter")