#https://school.programmers.co.kr/learn/courses/30/lessons/12985

from math import ceil
def solution(n,a,b):
    answer = 0
    while (a!=b):		#둘이 같은 번호를 배정받았다면 전라운드에서 영혼의 한타
        a=ceil(a/2)
        b=ceil(b/2)
        answer+=1		
    return answer