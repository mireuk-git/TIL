# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def solution(maps):
    x,y = -1,-1
    xl,yl = len(maps),len(maps[0])
    for i in range(xl):
        for j in range(yl):
            if maps[i][j]=="S":
                x,y = i,j
    
    destinations=["L","E"]
    s = 0
    for d in destinations:
        steps = [[99999]*yl for _ in range(xl)]
        steps[x][y] = 0
        queue = deque([(x,y)])
        while queue:
            x,y = queue.popleft()
            if maps[x][y]==d:
                s+=steps[x][y]
                break
            if x>0 and maps[x-1][y]!='X' and steps[x-1][y]>steps[x][y]+1:
                steps[x-1][y] = steps[x][y]+1
                queue.append((x-1,y))
            if x<xl-1 and maps[x+1][y]!='X' and steps[x+1][y]>steps[x][y]+1:
                steps[x+1][y] = steps[x][y]+1
                queue.append((x+1,y))
            if y>0 and maps[x][y-1]!='X' and steps[x][y-1]>steps[x][y]+1:
                steps[x][y-1] = steps[x][y]+1
                queue.append((x,y-1))
            if y<yl-1 and maps[x][y+1] != 'X' and steps[x][y+1]>steps[x][y]+1:
                steps[x][y+1] = steps[x][y]+1
                queue.append((x,y+1))
        if maps[x][y]!=d: return -1
    return s
    
solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])