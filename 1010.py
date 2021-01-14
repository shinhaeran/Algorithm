# def find_bridge(w,e):
#     l1 = [i+1 for i in range(e)] #동쪽
#     from itertools import permutations
#     permutation_li = list(permutations(l1,w))
#     answer = 0
#     for pl in permutation_li: # l[i] < l[i+1]
#         prev = pl[0]
#         flag = False
#         for i in range(1,len(pl)):
#             if pl[i] < prev:
#                 flag = True
#                 break
#             prev = pl[i]
#         if flag == False:
#             answer += 1
#     return answer

# n = int(input())
# # w,e = int(),int()

# for i in range(n):
#     w,e = map(int,input().split())
#     # print(w,e)
#     answer = find_bridge(w,e)
#     print(answer)

from math import factorial as fac

n = int(input())
for _ in range(n):
    w,e = map(int,input().split())
    result = fac(e)//fac(e-w)//fac(w)
    print(result)

