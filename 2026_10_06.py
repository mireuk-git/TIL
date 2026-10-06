# https://school.programmers.co.kr/learn/courses/30/lessons/135807

from math import gcd,sqrt
def solution(arrayA, arrayB):
    a=arrayA[0]
    for i in arrayA:
        a=gcd(i,a)
    ad=[a,0]
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: 
            ad.append(i)
            ad.append(a//i)
    ad.sort(reverse=True)

    b=arrayB[0]
    for i in arrayB:
        b=gcd(i,b)
    bd=[b,0]
    for i in range(2,int(sqrt(b))+1):
        if b%i==0:
            bd.append(i)
            bd.append(b//i)
    bd.sort(reverse=True)

    ap,bp=0,0
    while True:
        if ad[ap]==bd[bp]==0: return 0
        divided=False
        if ad[ap]>bd[bp]:
            for b in arrayB:
                if b%ad[ap]==0:
                    divided=True
                    break
            if not divided: return ad[ap]
            ap+=1
        else:
            for a in arrayA:
                if a%bd[bp]==0:
                    divided=True
                    break
            if not divided: return bd[bp]
            bp+=1

arrayA=[10,17]
arrayB=[5,20]
print(solution(arrayA,arrayB))