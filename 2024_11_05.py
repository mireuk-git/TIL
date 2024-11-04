# https://school.programmers.co.kr/learn/courses/30/lessons/178871#qna
def solution(players, callings):
    rank={player:i for i,player in enumerate(players)}
    for i in callings:
        current_rank=rank[i]
        rank[i]-=1
        rank[players[current_rank-1]]+=1
        tmp=players[current_rank]
        players[current_rank]=players[current_rank-1]
        players[current_rank-1]=tmp
    return players