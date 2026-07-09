# https://school.programmers.co.kr/learn/courses/30/lessons/160585
'''
def solution(board):
    count = {"O":0,"X":0}
    char = ["O","X"]
    bingo = False

    for i in range(3):
        for j in range(3):
            for c in char:
                if board[i][j] in c:
                    count[c]+=1
                    if board[i]==c*3: 
                        if bingo: return 0
                        bingo = True
                    elif board[0][j]+board[1][j]+board[2][j]==c*3:
                        if bingo: return 0
                        bingo = True
    
    if count["O"] not in [count["X"],count["X"]+1]:
        return 0
            
    return 1

board=["OOO",".O.","..O"]
print(solution(board))
'''
'''
def solution(board):
    bingo=False
    char = ["O","X"]
    #가로빙고 확인
    for i in range(3):
        for c in char:
            if board[i]==c*3:
                if bingo: return 0
                bingo = c
    #세로빙고 확인
    #빙고가 교차하는 경우도 룰상 불가능하진 않다
    bingo = False
    for i in range(3):
        for c in char:
            if board[0][i]+board[1][i]+board[2][i]==c*3:
                if bingo: return 0
                bingo = c
    #count
    count={"O":0,"X":0}
    for i in board:
        for c in i:
            if c in char:
                count[c]+=1

    for c in char:
        if board[0][0]+board[1][1]+board[2][2]==c*3:
            bingo=c
        if board[0][2]+board[1][1]+board[2][0]==c*3:
            bingo=c

    if bingo=="O":
        if count["O"]==count["X"]+1: return 1
    elif bingo=="X":
        if count["X"]==count["O"]: return 1
    elif count["O"] in [count["X"],count["X"]+1]:
        return 1
    else: return 0
'''
def is_win(board,player):
    for i in range(3):
        if board[i]==player*3:
            return True
        elif board[0][i]+board[1][i]+board[2][i]==player*3:
            return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    elif board[0][2]==board[1][1]==board[2][0]==player:
        return True
    return False

def solution(board):
    count=[0,0]
    for i in board:
        count[0]+=i.count("O")
        count[1]+=i.count("X")
    
    if is_win(board,"O"):
        if count[0]-count[1]!=1: return 0
        else: 
            if is_win(board,"X"): return 0
    elif is_win(board,"X"):
        if count[0]!=count[1]: return 0
    else:
        if count[0]-count[1] not in [0,1]:
            return 0
    return 1