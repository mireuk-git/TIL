# https://www.acmicpc.net/problem/4836
# 4836

while True:
    try:
        k=list(input().split())
    except EOFError: break
    l=[True, False, True, True, False]
    if "dip" in k: l[4]=True 
    if len(k)>=3 and k[-3] == "clap" and k[-2]=="stomp" and k[-1]=="clap": l[1]=True
    if "twirl" in k and "hop" not in k: l[2]=False
    if k[0]=="jiggle": l[3]=False
    if l[4]:
        for i in range(len(k)):
            if k[i] == "dip":
                if not ((i > 0 and k[i-1]=="jiggle") or (i > 1 and k[i-2]=="jiggle") or (i < len(k)-1 and k[i+1]=="twirl")):
                    l[0]=False
                    k[i]="DIP"

    if l.count(True) == 5: print("form ok: ",end='')
    else: 
        err=[]
        for i in range(len(l)): 
            if not l[i]: err.append(i+1)
        if len(err)==1:
            print(f"form error {err[0]}: ",end='')
        elif len(err)==2:
            print(f"form errors {err[0]} and {err[1]}: ",end='')
        else: 
            print("form errors ",end="")
            for i in range(len(err)-2):
                print(err[i],end=", ")
            print(f"{err[-2]} and {err[-1]}: ",end='')
    for i in k: print(i,end=" ")
    print()