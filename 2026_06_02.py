# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    targets.sort(key=lambda x: x[1])
    start = 0
    end = 0

    for s,e in targets:
        if s>=end:
            start = s
            end = e
            answer+=1
    return answer
