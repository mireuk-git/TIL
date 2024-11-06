# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    h,w=len(park)-1, len(park[0])-1
    for i in range(len(park)):
        if 'S' in park[i]: 
            answer=[i,park[i].index('S')]
            break
                
    for i in routes:
        d,l=i.split()
        l=int(l)
        if d=='N':
            if (answer[0]-l<0) or any(park[i][answer[1]]=='X' for i in range(answer[0]-1,answer[0]-l-1, -1)): 
                continue
            else: answer[0]-=l
        elif d=='S': 
            if (answer[0]+l>h) or any(park[i][answer[1]]=='X' for i in range(answer[0]+1,answer[0]+l+1)): 
                continue
            else: answer[0]+=l
        elif d=='E': 
            if (answer[1]+l>w) or any(park[answer[0]][i]=='X' for i in range(answer[1]+1,answer[1]+l+1)): 
                continue
            else: answer[1]+=l
        else: 
            if (answer[1]-l<0) or any(park[answer[0]][i]=='X' for i in range(answer[1]-1,answer[1]-l-1,-1)): 
                continue
            else: answer[1]-=l
        
    return answer