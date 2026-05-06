# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    result = [0]*len(photo)
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j]==name[k]:
                    result[i]+=yearning[k]
    return result

name=["may", "kein", "kain", "radi"]
yearning=[5, 10, 1, 3]
photo=[["may"],["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name,yearning,photo))