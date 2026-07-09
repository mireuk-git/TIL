# https://school.programmers.co.kr/learn/courses/30/lessons/169199
'''
from collections import deque

def solution(board,result):
    for i in range(len(board)):
        for j in range(i): 
            if board[i][j]=='R':
                pos = [i,j]

    def move(dir):
        r,c=pos
        while board[r][c]!='.':
            r+=dir[0]
            c+=dir[1]
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]): break
        r-=dir[0]
        c-=dir[1]
        return [r,c]
    #BFS
    queue=deque()
    count=0
    while True:
'''

def travel(ni,nj,nv,val,board):
    if val[ni][nj]!=-1 and val[ni][nj]<=nv:
        return
    val[ni][nj]=nv
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        i,j=ni,nj
        while True:
            if i+d[0]<0 or i+d[0]>len(board)-1 or j+d[1]<0 or j+d[1]:
                break
            elif board[i+d[0]][j]=='D' or board[i][j+d[1]]=='D':
                break
            i+=d[0]
            j+=d[1]
        if i!=ni or j!=nj:
            travel(i,j,nv+1,val,board)

def solution(board):
    start=[]
    goal=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                start=[i,j]
            if board[i][j]=='G':
                goal=[i,j]
        if start!=[] and goal!=[]: break
    
    val=[[-1]*len(board[0]) for _ in range(len(board))]
    travel(start[0],start[1],0,val,board)
    answer=val[goal[0]][goal[1]]
    return answer