# https://www.acmicpc.net/problem/25370
# 25370

def card_product(n):
    result=set()
    
    def dfs(product=1, depth=0):
        if depth==n:
            result.add(product)
            return
        for num in range(1,10):
            dfs(product*num,depth+1)
    dfs()
    return len(result)

n=int(input())
print(card_product(n))