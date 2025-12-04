# https://www.acmicpc.net/problem/12927
# 12927

feed = input()
status=['']
for i in feed:
    if i=='Y': status.append(True)
    elif i=='N': status.append(False)
count=0

for i in range(1,len(status)):
    if status[i]:
        for j in range(i,len(status),i):
            status[j]=not status[j]
        count+=1
print(count)
