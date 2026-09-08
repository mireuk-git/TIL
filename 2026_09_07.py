# https://school.programmers.co.kr/learn/courses/30/lessons/72412?language=python3
'''
def solution(info,query):
    for i in range(len(query)):
        query[i] = query[i].split(" and ")
        query[i] = query[i][:3] + query[i][3].split()

    result = [0]*len(query)
    for i in info:
        inf = i.split()
        for j in range(len(query)):
            if int(inf[4]) < int(query[j][4]): continue
            qual = True
            for k in range(4):
                if query[j][k] not in ["-",inf[k]]:
                    qual = False
                    break
            if qual: result[j]+=1
    return result
'''
from bisect import bisect_left

def solution(info, query):
    hashmap = {"-":0,
               "cpp":1,"java":2,"python":3,
               "backend":1,"frontend":2,
               "junior":1, "senior":2, 
               "chicken":1, "pizza":2
               }
    scores = [[] for _ in range(4*3*3*3)]
    for data in info:
        st = data.split()
        arr = (hashmap[st[0]]*3*3*3,
               hashmap[st[1]]*3*3,
               hashmap[st[2]]*3,
               hashmap[st[3]])
        score = int(st[4])
        for i in range(1<<4):
            idx = 0
            # 부분집합에 불이 켜진 경우
            for j in range(4):
                if i & (1 << j):
                    idx += arr[j]
            scores[idx].append(score)
            
    for i in range(4*3*3*3):
        scores[i].sort()

    answer=[]
    for string in query:
        q = string.split()
        idx = hashmap[q[0]]*3*3*3 + hashmap[q[2]]*3*3 +hashmap[q[4]]*3 + hashmap[q[6]]
        score = int(q[7])
        #score보다 크거나 같은 원소가 몇개 있는지..!
        answer.append(len(scores[idx]) - bisect_left(scores[idx],score))
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))