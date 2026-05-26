# https://school.programmers.co.kr/learn/courses/30/lessons/389479

from collections import deque

def solution(players, m, k):
    server=deque()
    count=0
    for t in range(24):
        while len(server)>0 and server[0]<=t: server.popleft()
        while players[t]>=(len(server)+1)*m:
            count+=1
            server.append(t+k)
    return count

players=[0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
m=1
k=1
print(solution(players,m,k))

