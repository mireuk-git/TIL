# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    f=[]
    for num in numbers:
        bit=1
        while num&bit:
            bit<<=1
        if bit>1: bit>>=1
        f.append(num+bit)
    return f

print(solution([2,7]))
