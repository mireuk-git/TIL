# https://www.acmicpc.net/problem/5149
# 5149

k = int(input())
for data_set in range(1,1+k):
    n,m = map(int,input().split())
    coords=[]
    for i in range(n): coords.append(tuple(map(int,input().split())))
    order = list(map(int,input().split()))
    max_x,max_y,min_x,min_y = '','','',''
    for i in order:
        if max_x == '' or max_x < coords[i-1][0]: max_x = coords[i-1][0]
        if min_x == '' or min_x > coords[i-1][0]: min_x = coords[i-1][0]
        if max_y == '' or max_y < coords[i-1][1]: max_y = coords[i-1][1]
        if min_y == '' or min_y > coords[i-1][1]: min_y = coords[i-1][1]
    cnt=0
    for i in coords:
        if min_x <= i[0] <= max_x and min_y <= i[1] <= max_y: cnt+=1
    print(f"Data Set {data_set}:")
    print(cnt)
    print()