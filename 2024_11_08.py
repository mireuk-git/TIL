#https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s=list(map(int,s.split()))
    answer = f'{min(s)} {max(s)}'
    return answer