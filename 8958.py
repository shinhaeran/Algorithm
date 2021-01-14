#O가 등장하면 -> score+=1 -> total += score -> X 등장하면 score 초기화
#OO -> 1+2 = 3
def cal_seq(case):
    score = 0
    total = 0
    for s in case:
        if s == 'O' :
            score += 1
            total += score
        else:
            score = 0
        prev_s = s
    print(total)

# def cal_seq(case):
#     case = case.split('X')
#     total = 0
#     for seq in case:
#         seq_score = 0
#         for s in seq:
#             seq_score += 1
#             total += seq_score
#     print(total)

num = int(input())
for i in range(num):
    cal_seq(input())