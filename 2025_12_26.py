# https://www.acmicpc.net/problem/27829
# 27829

import sys
input=sys.stdin.readline

t=int(input().strip())
for test_case in range(t):
    input()
    ng,nm=map(int,input().strip().split())
    g = sorted(list(map(int,input().strip().split())))
    m = sorted(list(map(int,input().strip().split())))
    gi,mi=0,0
    while (gi<ng and mi<nm):
        if g[gi]<m[mi]: gi+=1
        else: mi+=1
    if gi>=ng: print("MechaGodzilla")
    elif mi>=nm: print("Godzilla")
    else: print("uncertain")
