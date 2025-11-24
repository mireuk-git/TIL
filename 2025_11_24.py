# https://www.acmicpc.net/problem/10262
# 10262

def set_case(case):
    a1,b1,a2,b2 = map(int,input().split())
    next_case, case_limit=1, min(b1-a1,b2-a2)
    for i in range(a1+a2, b1+b2-case_limit+2):
        case[i]=next_case
        if next_case<case_limit: next_case+=1
    for i in range(b1+b2-case_limit+1,b1+b2+1):
        next_case-=1
        case[i]=next_case

case1 = {}
case2 = {}
set_case(case1)
set_case(case2)

winrate1=0
winrate2=0
for i in case1.keys():
    for j in case2.keys():
        if i>j: winrate1+=case1[i]*case2[j]
        elif i<j: winrate2+=case1[i]*case2[j]

if winrate1>winrate2: print("Gunnar")
elif winrate1<winrate2: print("Emma")
else:print("Tie")