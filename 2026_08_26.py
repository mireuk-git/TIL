# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    string = s
    count = [0,0]
    while string!="1":
        count[0]+=1
        count[1]+=string.count("0")
        string = string.replace("0","")
        string = bin(len(string))[2:]
    return count
print(solution("1111111"))