# https://www.acmicpc.net/problem/16218
# 16218

import sys
input=sys.stdin.readline

n,k=map(int,input().strip().split())
cummulate_a,cummulate_b=0,0
rebound=0
gg_flag=False
winner=0
overpowered=False

def overpower(a,b):
    global cummulate_a, cummulate_b, k, overpowered
    if overpowered: return False
    if cummulate_a + (int)(1.5*a) >= cummulate_b + b + 50:
        return True
    if cummulate_a + (int)(1.5*a) >= k and cummulate_b + b < k:
        return True
    else: return False

for i in range(n):
    line = input().strip()
    if not line: continue
    a, b = map(int, line.split())
    if gg_flag: continue

    cummulate_a-=rebound
    rebound=0
    if overpower(a,b): 
        rebound = (int)(a*1.5)-a
        a = (int)(a*1.5)
        overpowered=True
    cummulate_a+=a
    cummulate_b+=b
    
    if cummulate_a >= k and cummulate_b >= k:
        gg_flag=True
        if overpowered: winner = -1
        else: winner = 1
    if cummulate_a>=k or cummulate_a-cummulate_b>=50:
        winner = 1
        gg_flag = True
    elif cummulate_b>=k:
        winner = -1
        gg_flag = True

print(winner)
