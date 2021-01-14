n = int(input())
board = [False]*n
answer = int()

def pre_checking(row):#queen놓을 수 있는지 검사
    #세로,대각선 검사
    for i in range(row):
        if board[row]==board[i] or abs(board[row]-board[i])== row-i:
            return False
    return True

    
def n_queen(row):
    global answer
    # print(row,board)
    if row == n:
        answer += 1
        return 
    for i in range(n):
        board[row] = i
        if not pre_checking(row):
            continue
        n_queen(row+1)

n_queen(0)
print(answer)
