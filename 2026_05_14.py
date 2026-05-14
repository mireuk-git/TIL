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