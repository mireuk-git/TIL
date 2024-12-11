# https://school.programmers.co.kr/learn/courses/30/lessons/68645

'''
def solution(n):
    answer = [['' for j in range(i+1)] for i in range(n)]
    x,y=0,0
    direction=0
    max=sum([i for i in range(1,n+1)])+1
    for num in range(1, max):
        answer[x][y]=num
        if direction==0:
            if x==n-1 or answer[x+1][y]: 
                direction+=1
                y+=1
            else: x+=1
        elif direction==1:
            if y==n-1 or answer[x][y+1]: 
                direction+=1
                x-=1
                y-=1
            else: y+=1
        else: 
            if answer[x-1][y-1]: 
                direction=0
                x+=1
            else: 
                x-=1
                y-=1
    return answer
'''

def solution(n):
    answer = []

    mat = []
    target = 0
    for i in range(n):
        mat.append([])
        target += (i+1)

    direction = 0
    depth = 0
    R = 0
    U = 0

    cnt = n
    cnt2 = 0
    row = 0
    for i in range(1,target+1):
        if direction == 0:
            mat[row].insert(depth, i)
            cnt2 += 1
            if cnt2 < cnt:
                row += 1
            elif cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                direction = 1
                depth += 1

        elif direction == 1:
            mat[row].insert(depth+cnt2, i)    
            cnt2 += 1
            if cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                direction = 2
                R += 1
                row -= 1

        elif direction == 2:
            mat[row].insert(len(mat[row])-U, i)
            cnt2 += 1
            if cnt2 < cnt:
                row -= 1
            elif cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                direction = 0
                U += 1
                row += 1

    for i in range(len(mat)):
            answer+=mat[i]

    return answer