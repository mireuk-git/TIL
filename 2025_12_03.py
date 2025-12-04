# https://www.acmicpc.net/problem/9351
# 9351

import sys
input=sys.stdin.readline

t = int(input().strip())
for test_case in range(1,t+1):
    palin=[]
    s=input().strip()
    for x in range(len(s),1,-1):
        for i in range(len(s),x-1,-1):
            substring=s[i-x:i]
            if substring == substring[::-1]:
                palin.append(substring)
        if len(palin)>0: break
    print(f"Case #{test_case}:")
    for i in palin:
        print(i)
