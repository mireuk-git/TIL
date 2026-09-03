# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0,0]

    def quad(x,y,n):
        cur = arr[x][y]
        reduce = True
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j]!=cur: 
                    reduce=False
                    break
            if not reduce: break

        if reduce == False:
            half = n//2
            quad(x,y,half)
            quad(x+half,y,half)
            quad(x+half,y+half,half)
            quad(x,y+half,half)
        else: answer[cur]+=1

    quad(0,0,len(arr))
    return answer