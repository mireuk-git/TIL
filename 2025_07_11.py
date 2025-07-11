# https://www.acmicpc.net/problem/32292
# 32292
'''
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    repeat=True
    while repeat:
        repeat=False
        for i in range(len(s)-2):
            if s[i:i+3]=='ABB':
                s=s[:i]+'BA'+s[i+3:]
                repeat=True
    print(s)
'''
# https://www.acmicpc.net/problem/2578
# 2578
'''
num={}
for i in range(5):
    l=list(map(int,input().split()))
    for j in range(5):
        num[l[j]]=(i,j)
board=[[0]*5 for _ in range(5)]
turn=[]
for i in range(5): turn+=list(map(int,input().split()))

bingo=0
for i in range(25):
    x,y=num[turn[i]]
    board[x][y]=1

    line=True
    for xi in range(5):
        if board[xi][y]==0: 
            line=False
            break
    if line: bingo+=1

    line=True
    for yi in range(5):
        if board[x][yi]==0:
            line=False
            break
    if line: bingo+=1

    if x==y:
        line=True
        for j in range(5):
            if board[j][j]==0:
                line=False
                break
        if line: bingo+=1
    elif x==4-y:
        line=True
        for j in range(5):
            if board[j][4-j]==0:
                line=False
                break
        if line: bingo+=1

    if bingo>=3:
        print(i+1)
        break
'''

# 숫자 위치 저장
num = {}
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        num[row[j]] = (i, j)

# 사회자가 부르는 숫자들
turn = []
for _ in range(5):
    turn += list(map(int, input().split()))

# 체크판
board = [[0]*5 for _ in range(5)]

bingo = 0
for i in range(25):
    x, y = num[turn[i]]
    board[x][y] = 1
    count = 0

    # 가로, 세로
    if all(board[x][j] for j in range(5)):
        count += 1
    if all(board[i][y] for i in range(5)):
        count += 1

    # 대각선
    if x == y and all(board[d][d] for d in range(5)):
        count += 1
    if x + y == 4 and all(board[d][4 - d] for d in range(5)):
        count += 1

    bingo += count
    if bingo >= 3:
        print(i + 1)
        break

