# https://school.programmers.co.kr/learn/courses/30/lessons/176963
'''
def solution(name, yearning, photo):
    result = [0]*len(photo)
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j]==name[k]:
                    result[i]+=yearning[k]
    return result

name=["may", "kein", "kain", "radi"]
yearning=[5, 10, 1, 3]
photo=[["may"],["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name,yearning,photo))
'''

# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    result=[]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                result.append(i)
                break
        if len(result)==1: break

    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper)):
            if wallpaper[j][i]=='#':
                result.append(i)
                break
        if len(result)==2: break

    for i in range(len(wallpaper)-1,-1,-1):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                result.append(i+1)
                break
        if len(result)==3: break

    for i in range(len(wallpaper[-1])-1,-1,-1):
        for j in range(len(wallpaper)):
            if wallpaper[j][i]=='#':
                result.append(i+1)
                break
        if len(result)==4: break

    return result

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
print(solution(wallpaper))