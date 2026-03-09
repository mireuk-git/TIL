# https://www.acmicpc.net/problem/7600

string=input().lower()
while string != '#':
    d=set()
    for i in string: 
        if ord(i)>=97 and ord(i)<123: d.add(i)
    s=0
    print(len(d))
    string=input().lower()