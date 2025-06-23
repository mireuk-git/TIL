# https://www.acmicpc.net/problem/6615
# 6615

import sys
input=sys.stdin.readline

feed=input().strip()
while feed != "0 0":
    a,b=map(int,feed.split())
    a_list=[a]
    while a_list[-1]>1:
        if a_list[-1]%2: a_list.append(a_list[-1]*3+1)
        else: a_list.append(a_list[-1]//2)

    sb=0    
    b_tmp=b
    while b_tmp not in a_list:
        if b_tmp%2: b_tmp=b_tmp*3+1
        else: b_tmp//=2
        sb+=1

    print(f"{a} needs {a_list.index(b_tmp)} steps, {b} needs {sb} steps, they meet at {b_tmp}")
    feed=input().strip()