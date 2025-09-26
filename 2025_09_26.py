# https://www.acmicpc.net/problem/4649
# 4649

import sys
input=sys.stdin.readline
line=input().strip()
while line != "0":
    n,s=line.strip().split()
    n=int(n)
    count=0
    b=[]
    for i in s:
        if i in b:
            b.remove(i)
        elif len(b)<n:
            b.append(i)
        else: 
            count+=1
            b.append(i)
    count+=len(b)
    if count == 0: print("All customers tanned successfully.")
    else: print(f"{count} customer(s) walked away.")

    line=input().strip()