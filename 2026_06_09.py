from collections import Counter

class Robot:
    def __init__(self, points):
        self.points = points
        self.progress = 0
        self.n = len(points)-1
        self.pos = points[0]
    
    @property
    def active(self):
        return self.progress < self.n
    
    def move(self):
        if not self.active:
            return
        
        r_t, c_t = self.points[self.progress+1]
        r,c = self.pos

        if r_t<r: self.pos[0]-=1
        elif r<r_t: self.pos[0]+=1
        elif c_t<c: self.pos[1]-=1
        elif c<c_t: self.pos[1]+=1
        
        if self.pos == self.points[self.progress+1]:
            self.progress+=1

def solution(points, routes):
    count=0
    robots = []

    for route in routes:
        p = []
        for i in route:
            r,c=points[i-1]
            p.append([r,c])
        robots.append(Robot(p))
    
    while robots:
        c = Counter()
        for r in robots:
            c[tuple(r.pos)]+=1
    
        for k,v in c.items():
            if v>1: count+=1
    
        robots = [r for r in robots if r.active]

        for r in robots:
            r.move()

    return count

points=[[3, 2], [6, 4], [4, 7], [1, 4]]
routes=[[4, 2], [1, 3], [2, 4]]
print(solution(points,routes))