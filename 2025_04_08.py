# https://www.acmicpc.net/problem/31432
'''
n=int(input())
l=list(input().split())
print("YES")
print(int(l[-1])*11)
'''
# https://www.acmicpc.net/problem/4675
'''
dic=[]
while True:
    i=input()
    if i=="XXXXXX": break
    d={i:0 for i in range(97,123)}
    for c in i:
        d[ord(c)]+=1
    dic.append((i,d))

scrm=[]
while True:
    i=input()
    if i=="XXXXXX": break
    d={i:0 for i in range(97,123)}
    for c in i:
        d[ord(c)]+=1
    scrm.append(d)

for s in scrm:
    o=[]
    for d in dic:
        for i in range(97,123):
            if s[i]!=d[1][i]: 
                break
        if i==122: 
            o.append(d[0])
    if o: 
        o.sort()
        for i in o:print(i)
    else: print("NOT A VALID WORD")
    print("*"*6)
'''
'''
from collections import defaultdict

# 단어 사전 만들기
words_dict = defaultdict(list)

while True:
    word = input()
    if word == "XXXXXX":
        break
    key = ''.join(sorted(word))
    words_dict[key].append(word)

# 스크램블 처리
while True:
    scramble = input()
    if scramble == "XXXXXX":
        break
    key = ''.join(sorted(scramble))
    if key in words_dict:
        for w in sorted(words_dict[key]):
            print(w)
    else:
        print("NOT A VALID WORD")
    print("******")
'''