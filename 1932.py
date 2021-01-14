n = int(input())
triangle = list()
for _ in range(n):
    triangle.append(list(map(int,input().split())))
# print(triangle)
dp = triangle.copy()
for i in range(1,n):
    for j in range(i+1):
        dp[i][j] = max(triangle[i][j]+dp[i-1][min(i-1,j)],triangle[i][j]+dp[i-1][max(j-1,0)])
print(max(triangle[n-1]))

