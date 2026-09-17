# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def solution(users,emoticons):
    discount = [10,20,30,40]
    n = len(users)
    m = len(emoticons)

    def dfs(rate,d,buy):
        b = buy[:]
        if d>=0:
            for i in range(len(users)):
                if rate>=users[i][0]:
                    b[i] += (100-rate)*emoticons[d]//100
        
        if d<m-1:
            optimal = [0,0]
            for r in discount:
                branch = dfs(r,d+1,b)
                if optimal[0]<branch[0]:
                    optimal=branch
                elif optimal[0]==branch[0] and optimal[1]<branch[1]:
                    optimal=branch
            return optimal
        else:
            subscribe = 0
            for i in range(len(users)):
                if b[i]>=users[i][1]:
                    b[i]=0
                    subscribe+=1
            return [subscribe,sum(b)]

    result = dfs(0,-1,[0]*n)
    return result

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users,emoticons))