# http://acmicpc.net/problem/2456

n = int(input())
count=[[0,0,0,0] for i in range(3)]
score=[0,0,0]
for i in range(n):
    s = list(map(int,input().split()))
    for j in range(3):
        count[j][s[j]]+=1
        score[j]+=s[j]
count,score,i=zip(*sorted(zip(count,score,[1,2,3]),key=lambda x: (-x[1],-x[0][3],-x[0][2])))
if count[0][3]==count[1][3] and count[0][2]==count[1][2]:
    print(0,score[0])
else: print(i[0],score[0])