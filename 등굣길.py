def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    
    for x,y in puddles:
        dp[y][x] = 'X'
    dp[1][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1): # dp[i][j] = dp[i][j-1] + dp[i-1][j]
            if dp[i][j] == 'X':
                dp[i][j] = 0
                
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000007
    
    return dp[n][m]