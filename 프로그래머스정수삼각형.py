def solution(triangle):
    answer = 0
    # dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            try:
                if j-1 >= 0:
                    triangle[i][j] = max(triangle[i-1][j],triangle[i-1][j-1]) + triangle[i][j]
                else:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]      
            except:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
    # print(triangle)
    answer = max(triangle[-1])
    return answer