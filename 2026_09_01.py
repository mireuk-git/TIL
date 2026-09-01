# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k,ranges):
    # Collatz
    c = [k]
    while k>1:
        if k%2==1:
            k=3*k+1
        else: k//=2
        c.append(k)
    # integral
    inte = []
    end = len(c)-1
    for r in ranges:
        if r[0]>end+r[1]: 
            inte.append(-1.0)
            continue
        s=0.0
        for i in range(r[0],end+r[1]):
            s += (c[i]+c[i+1])/2
        inte.append(s)
    return inte