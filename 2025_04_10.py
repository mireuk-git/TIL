# https://www.acmicpc.net/problem/16020
'''
n=int(input())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))

row=False
column=False
if grid[0][0] < grid[0][1]: row=True
if grid[0][0] < grid[1][0]: column=True

if row and not column:
    grid=list(map(list,zip(*grid[::-1])))
elif not row and column:
    grid=list(map(list,zip(*grid)))[::-1]
elif not row and not column:
    grid=[_[::-1] for _ in grid[::-1]]

for i in grid:
    for j in i:
        print(j,end=' ')
    print()
'''
# https://www.acmicpc.net/problem/25206

rating={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum=0.0
units=0.0
for i in range(20):
    major,unit,grade=input().split()
    if grade!="P":
        unit=float(unit)
        sum+=unit*rating[grade]
        units+=unit
print(sum/units)