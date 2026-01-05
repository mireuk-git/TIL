# https://www.acmicpc.net/problem/26576
# 26576
'''
n=int(input())
month = {"January":"01","February":"02","March":"03","April":"04",
         "May":"05","June":"06","July":"07","August":"08",
         "September":"09","October":"10","November":"11","December":"12"}
for i in range(n):
    m,d,y=input().split()
    d=int(d[:-1])
    if m not in month.keys() or d<1 or d>31:
        print("Invalid")
        continue
    d=format(d,"02")
    y=format(int(y)%100,"02")
    print(f"{month[m]}/{d}/{y}")
'''

# https://www.acmicpc.net/problem/12260
# 12260

t=int(input())
for case in range(1,t+1):
    c,f,x = map(float,input().split())
    minimal_time = -1
    farm = 0
    while x>c:
        time=0
        farm+=1
        for i in range(farm):
            time += c/(2+f*i)
        time += x/(2+f*farm)
        if minimal_time>0 and time>=minimal_time: break
        else: minimal_time = time
    if x>c: minimal_time = min(minimal_time,x/2)
    else: minimal_time = x/2
    print(f"Case #{case}: {minimal_time:.7f}")