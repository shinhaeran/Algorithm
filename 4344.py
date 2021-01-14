def cal_seq(n,case):
    total = 0
    for score in case:
        total += score
    avg = total/n
    upper = 0
    # print(avg,total)
    for score in case:
        if score > avg:
            upper += 1
    # return round(upper/n *100,3)
    return upper/n *100
    

num = int(input())
for i in range(num):
    case = list(map(int,input().split()))
    # print(f'{cal_seq(case[0],case[1:])}%')
    print("%.3f%%" %cal_seq(case[0],case[1:]))

# a = int(input())
# y = 0
# for i in range(a):
#     b = list(map(int, input().split()))
#     score = 0
#     x = 0
#     for j in b[1:]:
#         score += j
#     for j in b[1:]:
#         if j > score/b[0]:
#             x += 1
#             y = x/b[0]*100
#     print(score,x)
#     print("%.3f%%" %y)