# https://www.acmicpc.net/problem/14383
# 14383

import sys
input=sys.stdin.readline

t=int(input().strip())
for test_case in range(1,t+1):
    s=input().strip()
    count=0
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            count+=1
            if s[i]=='-': s='+'*(i+1)+s[i+1:]
            else: s='-'*(i+1)+s[i+1:]
    if s[0]=='-': count+=1
    print(f"Case #{test_case}:",count)