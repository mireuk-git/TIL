# https://www.acmicpc.net/problem/24264
# 24264
'''
n=int(input())
print(n*n)
print(2)
'''
# https://www.acmicpc.net/problem/5342
# 5342

p={"Paper":57.99, "Printer":120.50, "Planners":31.25, "Binders":22.50, "Calendar":10.95, "Notebooks":11.20, "Ink":66.95}
i=input()
c=0
while i!="EOI":
    c+=p[i]
    i=input()
print("${0:.2f}".format(c))