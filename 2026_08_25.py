# https://school.programmers.co.kr/learn/courses/30/lessons/92342
'''
def dfs(info, result, start):
    n = sum(info)
    r = sum(result)

    best_result = [i for i in result]
    best_score = 0
    for i in best_result:
        if best_result[i]>0: best_score+=10-i

    for i in range(start,10):
        if r+info[i]>n: continue
        new_result = [j for j in result]
        new_result[i] = info[i]+1

        new_result = dfs(info,new_result,i+1)
        l_score,p_score = 0,0
        for j in range(10):
            if new_result[j]>info[j]:
                l_score+=10-j
            elif info[j]>0: p_score+=10-j
        score = l_score-p_score
        if score>best_score:
            best_score = score
            best_result = [j for j in new_result]
        elif score==best_score:
            for j in range(9,-1,-1):
                if best_result[j]<new_result[j]:
                    best_result = [k for k in new_result]
                    break
        print("new result:",new_result)
        print("best result:",best_result)
    return best_result
        


def solution(n,info):
    r = dfs(info,[0]*10,0)
    if sum(r)<n: 
        r[9]+=n-sum(r)
    return r

info = [2,1,1,1,0,0,0,0,0,0,0]	
print(solution(5,info))
'''

def solution(n,info):
    answer = [-1]
    max_diff = 0

    def dfs(idx,arrows,result):
        nonlocal answer, max_diff
        if idx==10:
            result[10]+=n-arrows
            p_score,l_score = 0,0
            for i in range(11):
                if info[i]<result[i]:
                    l_score+=10-i
                elif info[i]>0:
                    p_score+=10-i

            diff = l_score - p_score
            if max_diff<diff: 
                max_diff = diff
                answer = result[:]
            elif diff == max_diff and diff>0:
                for i in range(10,-1,-1):
                    if result[i] > answer[i]:
                        answer = result[:]
                        break
                    elif result[i]<answer[i]: break
            result[10]=0
            return
        dfs(idx+1,arrows,result)

        if arrows+info[idx]+1<=n:
            result[idx] = info[idx]+1
            dfs(idx+1,arrows+info[idx]+1,result)
            result[idx] = 0

    dfs(0,0,[0]*11)
    return answer