# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque
def solution(n, wires):
    answer=n
    matrix = [[]for i in range(n+1)]
    for w in wires:
        matrix[w[0]].append(w[1])
        matrix[w[1]].append(w[0])
    
    def bfs(s,end):
        visited=[0 for i in range(n+1)]
        visited[s]=1
        q=deque([s])
        cnt=1
        
        while q:
            x=q.popleft()
            for node in matrix[x]:
                if node!=end:
                    if visited[node]==0:
                        q.append(node)
                        visited[node]=1
                        cnt+=1
        return cnt
    
    for v in range(1,n+1):
        for node in matrix[v]:
            a=bfs(v,node)
            b=bfs(node,v)
            answer=min(answer,abs(a-b))
    return answer