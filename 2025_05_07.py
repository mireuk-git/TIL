# https://www.acmicpc.net/problem/14547
# 14547
'''
import sys
input=sys.stdin.readline
while True:
    res=input().strip()
    if res=='#': break
    res=res.split()[1]
    s=set()
    for i in range(len(res)-1):
        if res[i]==res[i+1]: s.add(res[i])
    
    s=sorted(list(s))
    if len(s)>1:
        print(f"{s[0]} {s[0]} glued and {s[1]} {s[1]} glued")
    elif len(s)>0:
        print(f"{s[0]} {s[0]} glued")
'''
# https://www.acmicpc.net/problem/9494
# 9494

import sys
input=sys.stdin.readline

while True:
    n=int(input().strip())
    if n==0: break
    m=0
    for _ in range(n):
        text=input()
        for i in range(m,len(text)):
            if text[i]==' ': 
                break
        m=i
    print(m+1)