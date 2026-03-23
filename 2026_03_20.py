# https://www.acmicpc.net/problem/12595

n = int(input())
for i in range(1,n+1):
    g = int(input())
    c = list(map(int,input().split()))
    s = set()
    for j in c:
        if j in s:
            s.remove(j)
        else: s.add(j)
    print(f"Case #{i}: {s.pop()}")