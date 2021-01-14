n,target = map(int,input().split())
m = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))

apps = []
for i in range(n):
    apps.append((m[i],c[i]))
# dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
dp = [0]+[0]+[10001]*(target-1)

for i in range(1,n+1):#1~n
    for j in range(target,0,-1): # 60~1
        if dp[j] != 10001: # 값의 변동이 있었다면
            if j+m[i] >= target: #target메모리를 초과한 경우,
                dp[target] = min(dp[target],dp[j]+c[i])
            else:
                if dp[j+m[i]] > dp[j] + c[i]: #j+m[i] 메모리일때 값을 갱신할지 선택 ->기존꺼보다 새로운게 적으면 갱신
                    dp[j+m[i]] = dp[j] + c[i]
print(dp[target])
# print(dp)


