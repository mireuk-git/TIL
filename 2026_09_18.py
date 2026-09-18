# https://school.programmers.co.kr/learn/courses/30/lessons/42890
'''
from collections import deque

def solution(relation):
    candidate = []
    c = len(relation)
    r = len(relation[0])
    #bfs
    queue = deque([[i] for i in range(r)])

    while queue:
        i = queue.popleft()

        view = []
        for re in relation:
            v=''
            for j in i:
                v+=re[j]+" "
            view.append(v)
        print(i,view)
        if len(view)==len(set(view)):
            if not any(set(c).issubset(i) for c in candidate):
                candidate.append(i)
                print("new candidate:", candidate)
        else:
            for j in range(i[-1]+1,r):
                queue.append(i+[j])
    return len(candidate)


relation = [["A", "BC", "E"],["AB", "C" ,"D"],["A", "C", "I"]]
print(solution(relation))
'''
from collections import deque

def solution(relation):
    candidate = []
    c = len(relation[0])
    # bfs
    queue=deque([[i] for i in range(c)])
    while queue:
        cols = queue.popleft()
        # 최소성 검사
        if any(set(i)<=set(cols) for i in candidate):
            continue
        # 유일성 검사
        view = [tuple(row[j] for j in cols) for row in relation]
        if len(view)==len(set(view)):
            candidate.append(cols)
        else:
            for j in range(cols[-1]+1,c):
                queue.append(cols+[j])
    return len(candidate)

relation = [["A", "BC", "E"],["AB", "C" ,"D"],["A", "C", "I"]]
print(solution(relation))