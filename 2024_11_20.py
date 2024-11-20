#https://school.programmers.co.kr/learn/courses/30/lessons/87390

'''
def solution(n, left, right):
    mat=[[0 for i in range(n)] for i in range(n)]
    for i in range(1,n+1):
        for j in range(i):
            mat[i-1][j]=i
            mat[j][i-1]=i
    
    array=[]
    for i in mat:
        array+=i
    
    answer = array[left:right+1]
    return answer
'''

def solution(n, left, right):
    answer = []
    for j in range(left, right+1):
        x,y = j//n+1, j%n+1
        if x>=y: answer.append(x)
        elif y>x: answer.append(y)
    return answer