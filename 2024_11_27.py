# https://school.programmers.co.kr/learn/courses/30/lessons/43165#qna

def solution(numbers, target):
    def dfs(i,sum):
        if i==len(numbers): 
            if sum==target: return 1
            else: return 0
        
        return dfs(i+1,sum+numbers[i])+dfs(i+1,sum-numbers[i])
    return dfs(0,0)