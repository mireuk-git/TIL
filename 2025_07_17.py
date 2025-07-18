# https://www.acmicpc.net/problem/10469
# 10469

def err_validator(x,y):
    for a,b in dir:
        tx,ty=x,y
        for i in range(7):
            tx+=a
            ty+=b
            if tx>7 or tx<0 or ty>7 or ty<0: break
            if board[tx][ty]=='*': 
                return True

board=[list(input()) for _ in range(8)]
valid=True
dir=[(1,0),(0,1),(1,1),(1,-1),(-1,0),(0,-1),(-1,-1),(-1,1)]
queen_cnt=0

for i in range(8):
    for j in range(8):
        if board[i][j]=='*':
            queen_cnt+=1
            if err_validator(i,j):
                valid=False
if queen_cnt!=8: 
    valid=False

if valid: print('valid')
else: print('invalid')
