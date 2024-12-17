# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(n,road,k):
    INF=10000000
    mat=[[INF for j in range(n+1)]for i in range(n+1)]
    for r in road:
        if mat[r[0]][r[1]]>r[2]: 
            mat[r[0]][r[1]]=r[2]
            mat[r[1]][r[0]]=r[2]
        
    def Dijkstra(mat):
        for i in range(1,len(mat)):
            for j in range(1,len(mat[i])):
                if j==i: continue
                for k in range(1,len(mat[i])):
                    if j==k: continue
                    if mat[i][j]>mat[i][k]+mat[k][j]:
                        mat[i][j]=mat[i][k]+mat[k][j]
        return mat
    
    mat=Dijkstra(mat)
    answer=1
    for i in range(1,len(mat[1])):
        if mat[1][i]<=k:
            answer+=1
    return answer

