# https://www.acmicpc.net/problem/24736

score=[]
for i in range(2):
    t,f,s,p,c=map(int,input().split())
    score.append(t*6+f*3+s*2+p*1+2*c)
for i in score: print(i,end=' ')