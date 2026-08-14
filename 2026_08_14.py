# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    d=[]
    char=['','A','E','I','O','U']
    for c1 in range(1,6):
        for c2 in char:
            for c3 in char:
                for c4 in char:
                    for c5 in char:
                        d.append(char[c1]+c2+c3+c4+c5)
    d=list(set(d))
    d.sort()
    return d.index(word)+1
print(solution("EIO"))