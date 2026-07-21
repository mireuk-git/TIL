# https://school.programmers.co.kr/learn/courses/30/lessons/148652

def check(i):
    if i%5==2: return 0
    elif i<5: return 1
    else: return check(i//5)

def solution(n,l,r):
    count=0

    for i in range(l-1,r):
        count+=check(i)
    return count