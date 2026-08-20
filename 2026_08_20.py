# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows,columns,queries):
    mat = []
    for i in range(rows+1):
        mat.append([])
        for j in range(columns+1):
            mat[i].append((i-1)*columns+j)

    answer=[]
    for q in queries:
        x1,y1,x2,y2 = q
        tmp = mat[x1][y1]
        m = tmp
        # rotation
        for r in range(x1,x2):
            mat[r][y1]=mat[r+1][y1]
            if m>mat[r][y1]: m=mat[r][y1]
        for c in range(y1,y2):
            mat[x2][c]=mat[x2][c+1]
            if m>mat[x2][c]: m=mat[x2][c]
        for r in range(x2,x1,-1):
            mat[r][y2]=mat[r-1][y2]
            if m>mat[r][y2]: m=mat[r][y2]
        for c in range(y2,y1,-1):
            mat[x1][c]=mat[x1][c-1]
            if m>mat[x1][c]: m=mat[x1][c]
        mat[x1][y1+1]=tmp
        answer.append(m)
    return answer
