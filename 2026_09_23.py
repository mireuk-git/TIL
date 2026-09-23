# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize,cities):
    time = 0
    cache = {}
    for i in range(len(cities)):
        cities[i]=cities[i].upper()
        if cities[i] in cache.keys():
            time+=1
        else:
            time+=5
        cache[cities[i]] = i
        if len(cache)>cacheSize:
            tmp=list(cache.items())
            tmp.sort(key = lambda x: x[1])
            del cache[tmp[0][0]]
    return time

cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(3,cities))