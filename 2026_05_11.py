def solution(video_len, pos, op_start, op_end, commands):
    def skip_op(pos):
        if op_start<=pos<op_end:
            pos=op_end
        p=list(map(int,pos.split(":")))
        return pos, p
    
    pos,p=skip_op(pos)
    for c in commands:
        if c=="next": 
            p[1]+=10
            if p[1]>59:
                p[0]+=1
                p[1]-=60
            pos = f"{p[0]:02d}:{p[1]:02d}"
            if pos>video_len: 
                pos=video_len
                p=list(map(int,pos.split(":")))
        elif c=="prev":
            p[1]-=10
            if p[1]<0:
                p[0]-=1
                p[1]+=60
            pos = f"{p[0]:02d}:{p[1]:02d}"
            if pos<"00:00": 
                pos="00:00"
                p=list(map(int,pos.split(":")))
        pos,p=skip_op(pos)
        print(p)

    answer = pos
    return answer

video_len="30:00"
pos="00:00"
op_start="00:10"
op_end="00:15"
commands=["next"]
print(solution(video_len,pos,op_start,op_end,commands))