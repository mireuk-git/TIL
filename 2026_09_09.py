# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    answer=w*h
    def gcd(a,b):
        while b>0:
            if b>a: a,b = b,a
            tmp = b
            b = a%b
            a = tmp
        return a
    n=gcd(w,h)
    answer-=w+h-n
    return answer

print(solution(8,12))