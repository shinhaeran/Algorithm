n = int(input())
def pado(n):
    dp = [0,1,1,1,2,2]
    if n < 6:
        return dp[n]
    else: # dp[n] = dp[n-1] + dp[n-5]
        a,b = dp[5], dp[1] # n = 6
        c = 0
    
        for i in range(6,n+1):
            c = a + b
            a = c
            b = dp[i%5+1]
            if i%5 == 0:
                dp[5] = c
            else:
                dp[i%5] = c
        return c




for _ in range(n):
    target = int(input()) 
    print(pado(target))

# import sys
# N = int(sys.stdin.readline())
# dp = [0, 1, 1, 1, 2]
# for i in range(5, N+1):
#     dp.append(dp[i-1] + dp[i-5])
# print(dp[N])