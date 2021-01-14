def tiling(n):
    if n ==0 or n == 1:
        return 1
    if n == 2:
        return 3
    prev1,prev2 = 3,1
    for _ in range(3,n+1):
        result = prev1 + prev2*2
        prev1,prev2 = result,prev1
    return result

#input
input_num = []
# dp = [1] + [0 for _ in range(max(input_num))]
# dp[1],dp[2] = 1,3 
while True:
    try:
        print(tiling(int(input())))
    except:
        break

     