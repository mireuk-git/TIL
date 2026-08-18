# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def distancing(place):
    for r in range(5):
        for c in range(5):
            if place[r][c]=='P':
                if r<4 and c>0 and place[r+1][c-1]=='P': #DiagonalLeft
                    if place[r+1][c]!='X' or place[r][c-1]!='X': return 0
                for i in range(1,3): #Down
                    if r+i>=5: break #OutOfBoundaries
                    if place[r+i][c]=='X': break
                    if place[r+i][c]=='P': return 0
                if r<4 and c<4 and place[r+1][c+1]=='P': #DiagonalRight
                    if place[r+1][c]!='X' or place[r][c+1]!='X': return 0
                for i in range(1,3): #Right
                    if c+i>=5: break #OutOfBoundaries
                    if place[r][c+i] == 'X': break
                    if place[r][c+i] == 'P': return 0
    return 1

def solution(places):
    answer=[]
    for place in places:
        answer.append(distancing(place))
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))