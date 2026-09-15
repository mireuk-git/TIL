# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    routes = set()
    pos = [0,0]
    for d in dirs:
        route = [tuple(pos)]
        if d == "R":
            if pos[0]<5: pos[0]+=1
            else: continue
        elif d == "L":
            if pos[0]>-5: pos[0]-=1
            else: continue
        elif d == "U":
            if pos[1]<5: pos[1]+=1
            else: continue
        elif d == "D":
            if pos[1]>-5: pos[1]-=1
            else:continue
        route.append(tuple(pos))
        route.sort(key = lambda x: [x[0],x[1]])
        routes.add(str(route))
    return len(routes)

print(solution("LULLLLLLU"))