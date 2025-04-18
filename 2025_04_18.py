# https://www.acmicpc.net/problem/13733
# 13733

sq=[]
for _ in range(3):
    sq.append(tuple(map(int,input().split())))
ans="NO"

# 1st form
if sq[0][0]==sq[1][0] and sq[0][0]==sq[2][0] and sq[0][0]==sq[0][1]+sq[1][1]+sq[2][1]:
    ans="YES"

# 2nd form
for i in range(2):
    for j in range(2):
        if sq[0][0]==sq[1][i]+sq[2][j] and sq[0][0]==sq[0][1]+sq[1][(i+1)%2] and sq[1][(i+1)%2]==sq[2][(j+1)%2]:
            ans="YES"

print(ans)