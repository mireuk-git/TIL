# https://www.acmicpc.net/problem/2765
# 2765

trip = 0
while True:
    radius, revol, time = map(float,input().split())
    revol=int(revol)
    if revol == 0: break
    trip+=1

    pi = 3.1415927
    distance = pi*radius*revol/5280/12
    mph = distance/time*3600
    print("Trip #{}: {:.2f} {:.2f}".format(trip,distance,mph))
