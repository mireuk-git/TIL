# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill,skill_trees):
    count = 0
    for s in skill_trees:
        i = 0
        avail = True
        for c in s:
            if c in skill:
                if c == skill[i]:
                    i+=1
                else: 
                    avail = False
                    break
        if avail: count+=1
    return count

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
