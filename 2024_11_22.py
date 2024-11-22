# https://school.programmers.co.kr/learn/courses/30/lessons/131127#qna

def solution(want, number, discount):
    answer=0
    for i in range(len(discount)-9): 
        avail=discount[i:i+10]
        if all(num <= avail.count(product) for num,product in zip(number,want)):
            answer+=1
    return answer