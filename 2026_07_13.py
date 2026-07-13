# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def solution(maps):
    rl,cl = len(maps)+2,len(maps[0])+2
    container = [["X"]*cl for _ in range(rl)]
    for i in range(rl-2):
        for j in range(cl-2):
            container[i+1][j+1]=maps[i][j]
    visited = [[False]*cl for _ in range(rl)]

    score=[]
    for i in range(1,rl-1):
        for j in range(1,cl-1):
            if not visited[i][j] and container[i][j]!="X":
                s = int(container[i][j])
                visited[i][j] = True
                queue = deque([(i,j)])
                while queue:
                    r,c = queue.popleft()
                    if not visited[r+1][c] and container[r+1][c]!="X":
                        visited[r+1][c] = True
                        s+=int(container[r+1][c])
                        queue.append((r+1,c))
                    if not visited[r-1][c] and container[r-1][c]!="X":
                        visited[r-1][c] = True
                        s+=int(container[r-1][c])
                        queue.append((r-1,c))
                    if not visited[r][c+1] and container[r][c+1]!="X":
                        visited[r][c+1] = True
                        s+=int(container[r][c+1])
                        queue.append((r,c+1))
                    if not visited[r][c-1] and container[r][c-1]!="X":
                        visited[r][c-1] = True
                        s+=int(container[r][c-1])
                        queue.append((r,c-1))
                if s>0: score.append(s)

    if not score: return [-1]
    score.sort()
    return score
    
solution(["X591X","X1X5X","X231X", "1XXX1"])
