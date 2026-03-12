# https://www.acmicpc.net/problem/11195

string = input()
count = 0
odd = False
for i in range(97,123):
    if string.count(chr(i))%2:
        if not odd: odd = True
        else: count+=1
print(count)
