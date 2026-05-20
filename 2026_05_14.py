'''
def solution(mats,park):
    mats.sort(reversed=True)
    for m in mats:
        for x in range(len(park)-m+1):
            for y in range(len(park[x])-m+1):
                if park[x][y]=='-1':
                    success=True
                    for i in range(m):
                        for j in range(m):
                            if park[x+i][y+j]!='-1':
                                success=False
                                break
                        if not success: break
                    if success: return m
    return -1
'''

# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    hp=health
    t=0
    for a in attacks:
        if hp<health:
            if a[0]-t>bandage[0]: hp+=min((a[0]-t-1)*bandage[1]+(a[0]-t-1)//bandage[0]*bandage[2],health-hp)
            else: hp+=min((a[0]-t-1)*bandage[1],health-hp)
        hp-=a[1]
        if hp<=0: return -1
        t=a[0]
    return hp
'''
bandage=[3,2,7]
health=20
attacks=[[1, 15], [5, 16], [8,6], [11, 5]]
print(solution(bandage,health,attacks))
'''
'''
bandage=[5,1,5]
health=30
attacks=[[2,10],[9,15],[10,5],[11,5]]
print(solution(bandage,health,attacks))
'''
'''
bandage=[4,2,7]
health=20
attacks=[[1,15],[5,16],[8,6]]
print(solution(bandage,health,attacks))
'''
bandage=[1,1,1]
health=5
attacks=[[1,2],[3,2]]
print(solution(bandage,health,attacks))