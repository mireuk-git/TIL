#https://school.programmers.co.kr/learn/courses/30/lessons/133502#qna

'''
def solution(ingredient):
    answer = 0
    order=[1,2,3,1]
    index_left=0
    while 1 in ingredient[index_left:len(ingredient)-3]:
        index_left=ingredient.index(1,index_left)
        burger_flag=True
        for i in range(1,4):
            if ingredient[index_left+i] != order[i]:
                burger_flag=False
                break
        if burger_flag:
            for i in range(4):
                del ingredient[index_left]
            index_left=0
            answer+=1
        index_left+=1
    return answer
'''

def solution(ingredient):
    answer = 0
    st = [] 
    for i in range(len(ingredient)):
        st.append(ingredient[i])
        if(len(st)>=4 and ingredient[i] == 1):  
            n = len(st)
            if st[-2] == 3 and st[-3] == 2 and st[-4]==1: 
                for i in range(4):
                    st.pop()
                answer+=1
    return answer