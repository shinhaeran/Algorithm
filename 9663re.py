n = int(input())
board1 = [False]*n #세로줄
board2 = [False]*(2*n-1)# / 
board3 = [False]*(2*n-1)# \ 
answer = int()

def pre_checking(row,i):#queen놓을 수 있는지 검사
    #세로,대각선 검사
    if (board1[i] or board2[row+i] or board3[row-i+n-1]):
        return False
    return True
    
def n_queen(row):
    global answer
    # print(row,board)
    if row == n:
        answer += 1
        return 
    for i in range(n):
        if not pre_checking(row,i):
            continue
        board1[i] = True
        board2[row+i] = True
        board3[row-i+n-1] = True
        n_queen(row+1)
        board1[i] = False
        board2[row+i] = False
        board3[row-i+n-1] = False

n_queen(0)
print(answer)
