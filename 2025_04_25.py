# https://www.acmicpc.net/problem/11270
# 11270
'''
from collections import deque

n,k=map(int,input().split())
q=deque([])
for _ in range(n):
    request=int(input())
    server.append([request])
    request=int(input())
    for s in range(len(server)):
        if server[s][0]+1000 > request:
            if len(server[s])<k: 
                server[s].append()
    else: 
        server.append(request)
        q[-1]+=1
'''

from collections import deque

n,k=map(int,input().split())
times=[int(input()) for _ in range(n)]

q=deque()
max_request=0
for t in times:
    while q and q[0]<=t-1000:
        q.popleft()
    q.append(t)
    max_request=max(max_request,len(q))

print((max_request+k-1)//k)