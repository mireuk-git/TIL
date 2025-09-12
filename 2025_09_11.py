# https://www.acmicpc.net/problem/29808
# 29808

s=int(input())
l=[]
seen=set()

if s%4763==0: 
    s//=4763
    X,Y=[508,108],[305,212]

    for diff1 in range(200):
        for x in X:
            for y in Y:
                if (s-(diff1*x))%y==0:
                    diff2=(s-(diff1*x))//y
                    if diff2>=0 and diff2<=200 and (diff1,diff2) not in seen:
                        l.append((diff1,diff2))
                        seen.add((diff1,diff2))

print(len(l))
for a,b in l:
    print(a,b)