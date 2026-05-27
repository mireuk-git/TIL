# https://school.programmers.co.kr/learn/courses/30/lessons/388353

from collections import deque

def accessible(r,c,container):
    if container[r-1][c] and container[r+1][c] and container[r][c-1] and container[r][c+1]:
        return False
    return True

def solution(storage, requests):
    width = len(storage[0])+2
    height = len(storage)+2
    container=[[0]*width for _ in range(height)]
    for r in range(1,height-1):
        for c in range(1,width-1):
            container[r][c]=storage[r-1][c-1]

    for req in requests:
        if len(req)==1: #lift
            for r in range(1,height-1):
                for c in range(1,width-1):
                    if container[r][c] == req and accessible(r,c,container):
                        container[r][c] = 1
    
        else: #crane
            for r in range(1, height-1):
                for c in range(1, width-1):
                    if container[r][c] == req[0]:
                        container[r][c] = 1

        # BFS, secure route
        queue = deque()
        queue.append((0,0))
        visited=[[0]*width for _ in range(height)]
        while queue:
            r,c = queue.popleft()
            container[r][c]=0
            if not visited[r][c+1] and container[r][c+1] in [0,1]:
                queue.append((r,c+1))
                visited[r][c+1]=1
            if not visited[r][c-1] and container[r][c-1] in [0,1]:
                queue.append((r,c-1))
                visited[r][c-1]=1
            if not visited[r+1][c] and container[r+1][c] in [0,1]:
                queue.append((r+1,c))
                visited[r+1][c]=1
            if not visited[r-1][c] and container[r-1][c] in [0,1]:
                queue.append((r-1,c))
                visited[r-1][c]=1

    count=0
    for r in range(1,height-1):
        for c in range(1,width-1):
            if container[r][c] not in [0,1]:
                count+=1
    return count