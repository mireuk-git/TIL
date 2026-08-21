# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def judge(s):
    opening=['(','{','[']
    end={')':'(','}':'{',']':'['}
    stack=[]
    for c in s:
        if c in opening:
            stack.append(c)
        else:
            if len(stack)==0 or end[c] != stack[-1]:
                return False
            stack.pop()
    if len(stack): return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        string = s[i:]+s[:i]
        if judge(string): answer+=1
    return answer

print(solution("{{{{"))