# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    n=len(board)
    count=0
    dh,dw = [0,1,-1,0],[1,0,0,-1]
    for k in range(4):
        h_ch,w_ch=h+dh[k],w+dw[k]
        if 0<=h_ch<n and 0<=w_ch<n :
            if board[h][w]==board[h_ch][w_ch]:
                count+=1
    return count

