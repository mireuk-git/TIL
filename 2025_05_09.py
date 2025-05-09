# https://www.acmicpc.net/problem/2606
# 2606
'''
com=int(input())
infected=set()
infected.add(1)
n=int(input())
for _ in range(n):
    branch=list(map(int,input().split()))
    if branch[0] in infected:
        infected.add(branch[1])
print(len(infected)-1)
'''
'''
from collections import deque

com=int(input())
connec=[[] for i in range(com+1)]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    connec[a].append(b)
    connec[b].append(a)

visited=[False]*(com+1)

count=0
queue=deque([1])
visited[1]=True
while queue:
    cur=queue.popleft()
    for neighbor in connec[cur]:
        if not visited[neighbor]:
            visited[neighbor]=True
            queue.append(neighbor)
            count+=1

print(count)
'''
com=int(input())
graph=[[] for i in range(com+1)]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(com+1)

def dfs(x):
    visited[x]=True
    count=1
    for neighbor in graph[x]:
        if not visited[neighbor]:
            count+=dfs(neighbor)
    return count

print(dfs(1)-1)