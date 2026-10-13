# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def eratos(n):
    sieve = [True]*(n+1)
    sieve[0],sieve[1] = False,False

    end = int(n**0.5)+1
    for i in range(2,end):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return [i for i in range(n+1) if sieve[i]]

def solution(numbers):
    # 만들 수 있는 숫자
    s = set()
    for i in range(1,len(numbers)+1):
        s = s.union(set(permutations(numbers,i)))
    num=set()
    for i in s:
        num.add(int(''.join(i)))
    # 최댓값까지의 에라토스테네스
    sieve = eratos(max(num))

    # 소숫값과 카드로 만들 수 있는 숫자의 교집합
    result = set(sieve).intersection(num)
    return len(result)

numbers="17"
print(solution(numbers))