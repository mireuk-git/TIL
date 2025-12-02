# https://www.acmicpc.net/problem/14291
# 14291

import sys
input = sys.stdin.readline

t=int(input().strip())
for test_case in range(1,1+t):
    s = input().strip()
    l = len(s)
    i,j = map(int,input().strip().split())
    
    c = s.count('B')*(j//l-(i+l-2)//l)
    i,j = (i-1)%l,(j-1)%l
    if c == 0 and i<j: c = s[i:j+1].count('B')
    else:
        if i != 0: 
            c+=s[i:].count('B')
        if j != l-1: 
            c+=s[:j+1].count('B')
    print(f"Case #{test_case}:",c)
