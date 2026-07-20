# https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''
def solution(storey):
    s = [0]
    for i in str(storey): s.append(int(i))
    for i in range(len(s)-1,0,-1):
        if s[i]>5:
            s[i-1]+=1
            s[i]=10-s[i]
    return sum(s)

print(solution(2554))
'''

def solution(storey):
    count = 0
    while storey:
        storey, r = storey//10, storey%10

        if r<5 or (r==5 and storey%10<5): count+=r
        else: 
            count+=10-r
            storey+=1
    return count
