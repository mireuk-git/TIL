# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    from math import sqrt
    answer = 0
    for i in range(1,number+1):
        n_d=0
        if i<=2: n_d=i
        else:
            for j in range(1,int(sqrt(i))+1):
                if i%j==0: n_d+=2
            if i%sqrt(i)==0: n_d-=1
        if n_d<=limit: answer+=n_d
        else: answer+=power
    return answer