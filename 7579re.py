n,target = map(int,input().split())
# target메모리 채울 때 까지 app 비활성화 -> cost 가장 적게! 
# => dp[i][j] : i번째 앱 까지 고려했을때, j cost가 소비되는 메모리의 최댓값
m = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))

dp = [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]
answer = sum(c)
for i in range(1,n+1): # 1~n
    for j in range(1,sum(c)+1): # 1~sum(c)
        if j - c[i] >= 0:
            dp[i][j] = max(dp[i-1][j-c[i]] + m[i],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= target:
            answer = min(answer,j)

if target == 0:
    print(0)
else:
    print(answer)


    