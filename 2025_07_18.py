# https://www.acmicpc.net/problem/15017
# 15017

n=int(input())
pool=[]
for _ in range(n):
    name,first_leg,later_leg=input().split()
    pool.append((name,float(first_leg),float(later_leg)))

minimum_time=float('inf')
best=[]
pool.sort(key=lambda runner: runner[2])

for i in range(n):
    roster=[pool[i][0]]
    time=pool[i][1]
    count=1
    for runner in pool:
        if runner[0]==roster[0]: continue
        roster.append(runner[0])
        time+=runner[2]
        count+=1
        if count>=4: break

    if count==4 and time<minimum_time:
        minimum_time=time
        best=roster
del time, roster, count, i, runner

print(minimum_time)
for i in best: print(i)



    
