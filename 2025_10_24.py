# https://www.acmicpc.net/problem/28446
# 28446

import sys
input=sys.stdin.readline

m=int(input().strip())
location={}
for i in range(m):
    request = input().strip()
    op,request = request.split(' ',1)
    if op=='1':
        x,w=map(int,request.split())
        location[w]=x
    if op=='2':
        w = int(request)
        print(location[w])