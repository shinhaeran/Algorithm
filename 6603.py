from itertools import permutations
def select_num(lotto,n,nums):
    if len(nums) == len(lotto):
        print(nums)
        return
    # range(n,len(lotto)-(6-n-1))
    for e in lotto[n:-(6-n-2)]:
        temp = nums[:]
        temp.append(e)
        select_num(lotto,n+1,temp)


while True:
    l1 = input().split()
    n = int(l1[0])
    if n == 0:
        break
    # lotto = permutations(l1[1:-1],6)
    # print(list(lotto))
    lotto = l1[1:-1]
    for e in lotto[0:len(lotto)-6 + 1]: # 0~ 7-6 : 0~1
        # print(e)
        select_num(lotto,1,[e])
    print()