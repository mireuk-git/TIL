# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    total,length,left=0,0,-1
    if k in sequence: return [sequence.index(k),sequence.index(k)]
    
    for i in range(len(sequence)-1,-1,-1):
        total+=sequence[i]
        while total>k:
            total-=sequence.pop()
        if total==k:
            if length and len(sequence)-1-i>length: return [left,left+length]
            else: 
                length=len(sequence)-1-i
                left = i
    return [left,left+length]