b_count = int()
w_count = int()

def compare_board(b_board,w_board,y,x,board):
    global b_count,w_count
    for j in range(0,8):
        for i in range(0,8):
            if board[j+y][x+i] != b_board[j][i]:
                b_count+=1
            if board[j+y][x+i] != w_board[j][i]:
                w_count+=1
    
board = list()

b_board = list()
w_board = list()

h,w = map(int,input().split())

b_line = str()
w_line = str()

for i in range(w):
    if i%2 == 0:
        b_line += 'B'
        w_line += 'W'
    else:
        b_line += 'W'
        w_line += 'B'

for i in range(h):
    board.append(input())
    if i%2 == 0:
        b_board.append(b_line)
        w_board.append(w_line)
    else:
        b_board.append(w_line)
        w_board.append(b_line)

answer = 9999999999
for y in range(h-7):
    for x in range(w-7):
        compare_board(b_board,w_board,y,x,board)
        answer = min(b_count,w_count,answer)
        b_count = 0
        w_count = 0
        
print(answer)