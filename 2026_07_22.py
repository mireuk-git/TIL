# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data,col,row_begin,row_end):
    # 2. sort
    data.sort(key = lambda x: (x[col-1], -x[0]))
    # 3. define s
    s=[]
    for i in range(row_begin-1, row_end):
        n=0
        for j in data[i]:
            n+=j%(i+1)
        s.append(n)
    # 4. bitwise XOR
    b = s[0]
    for i in s[1:]:
        b=b^i
    return b


data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
print(solution(data,2,2,3))