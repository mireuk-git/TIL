# https://www.acmicpc.net/problem/16493
# 16493

def searchtree(ch,n,d=0,p=0):
    if d==len(ch)-1: 
        return p
    a=searchtree(ch,n-ch[d][0],d+1,p+ch[d][1])
    b=searchtree(ch,n,d+1,p)
    if a>b: print(f"{d}: yes")
    else: print(f"{d}: no")
    return max(a,b)


n,m=map(int,input().split())
ch=[]
for _ in range(m):
    ch.append(list(map(int,input().split())))
print(searchtree(ch,n))