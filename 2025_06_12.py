# https://www.acmicpc.net/problem/31823
# 31823
'''
n,m=map(int,input().split())
l=[]
streaks=[]
for _ in range(n):
    feed=input()
    rstreak=0
    mstreak=0
    for i in range(0,2*m,2):
        if feed[i]=='.':
            rstreak+=1
            mstreak=max(rstreak,mstreak)
        else: rstreak=0
    streaks.append(mstreak)
    l.append((mstreak,feed[2*m:],))
print(len(set(streaks)))
for i in l:
    print(i[0],i[1])
'''
# https://www.acmicpc.net/problem/2960
# 2960
'''
n,k=map(int,input().split())
l=[i for i in range(2,1+n)]
c=0
idx=0
while c<k:
    while l[idx]==-1: idx+=1
    c+=1
    i=idx
    while c<k and i<n-1-l[idx]:
        i+=l[idx]
        if l[i]!=-1:
            c+=1
            if c==k: break
            l[i]=-1
    if c==k: print(l[i])
    l[idx]=-1
'''

n,k=map(int,input().split())
numbers=[True]*(n+1)
count=0

done=False
for i in range(2,n+1):
    if numbers[i]:
        for j in range(i,n+1,i):
            if numbers[j]:
                numbers[j]=False
                count+=1
                if count==k:
                    print(j)
                    done=True
                    break
    if done: break