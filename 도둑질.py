def solution(money):
    answer = 0
    N = len(money)
    dp1 = [0 for _ in range(N)]
    dp1[0] = money[0]
    # dp1[1] = money[1] #dp[i] = max(dp[n-2]+money[i] , dp[n-1])
    dp1[1] = max(money[0],money[1])
    
    for i in range(2,N-1):
        dp1[i] = max(dp1[i-2]+money[i] , dp1[i-1])
    # dp1[N-1] = max(dp1[N-3]+money[N-1]-dp1[0] , dp1[N-2])    
        
        
    dp2 = [0 for _ in range(N)]
    dp2[1] = money[1]
    for i in range(2,N):
        dp2[i] = max(dp2[i-2]+money[i] , dp2[i-1])
    # dp[N-1] = max(dp[N-3]+money[N-1]-dp[0],dp[N-2])
    # print(dp)
    # answer = max(dp1[N-1],dp2[N-1])
    # answer = max(max(dp1),max(dp2))
    answer = max(dp1[N-2],dp2[N-1])
    return answer