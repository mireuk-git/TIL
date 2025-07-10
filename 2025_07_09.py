# https://www.acmicpc.net/problem/9063
# 9063
'''
n=int(input())
coord=[]
x_list=[]
y_list=[]
for i in range(n):
    x,y=map(int,input().split())
    x_list.append(x)
    y_list.append(y)
x_list.sort()
y_list.sort()
a=(x_list[-1]-x_list[0])*(y_list[-1]-y_list[0])
print(a)
'''
# https://www.acmicpc.net/problem/14730
# 14730

n=int(input())
r=0
for i in range(n):
    c,k=map(int,input().split())
    r+=c*k
print(r)