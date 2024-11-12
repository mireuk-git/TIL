#https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = [brown//2-3, 1]
    while (answer[0])*(answer[1])!=yellow:
        answer[0]-=1
        answer[1]+=1
    answer[0]+=2
    answer[1]+=2
    return answer