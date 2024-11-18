# https://school.programmers.co.kr/learn/courses/30/lessons/131701

'''
def solution(elements):
    answer = list(elements)
    for i in range(2,len(elements)):
        for j in range(len(elements)):
            s=0
            for k in range(i):
                s+=elements[(j+k)%len(elements)]
            answer.append(s)
    answer.append(sum(elements))
    answer=set(answer)       
    return len(answer)
'''

def solution(elements):
    circular=elements*2
    answer=[]
    for i,n in enumerate(elements):
        answer.append(n)
        for j in circular[i+1:i+len(elements)]:
            n+=j
            answer.append(n)      
    return len(set(answer))