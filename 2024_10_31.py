#https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    for i in s:                     
        o=ord(i)
        for j in range(index):          #s의 알파벳을 index만큼 뒤로 보냄
            o+=1
            if o>ord('z'):              #z를 넘어갈경우 다시 a로
                o=o-ord('z')+96
            while chr(o) in skip:       #skip은 건너뜀
                o+=1
                if o>ord('z'):          #z를 넘어갈경우 다시 a로
                    o=o-ord('z')+96
        answer+=chr(o)
    return answer