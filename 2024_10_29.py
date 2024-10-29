def solution(s):
    answer = 0
    i=0
    while (i<len(s)):
        x=s[i]
        count=[0,0]
        while (i<len(s)):
            if x==s[i]:
                count[0]+=1
            else:
                count[1]+=1
            i+=1
            if count[0]==count[1]:
                break
        answer+=1
    return answer