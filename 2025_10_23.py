# https://www.acmicpc.net/problem/4757
# 4757

n=int(input())
winner=''
winner_point=[0,0]
for i in range(n):
    name,problem=input().split(" ",1)
    problem=list(map(int,problem.split()))
    solved,penalty=0,0
    for j in range(1,8,2):
        if problem[j]>0:
            solved+=1
            penalty+=problem[j]+(problem[j-1]-1)*20
    if winner=='' or winner_point[0] < solved or (winner_point[0] == solved and winner_point[1] > penalty):
        winner_point=[solved,penalty]
        winner = name
print(winner,winner_point[0],winner_point[1])
