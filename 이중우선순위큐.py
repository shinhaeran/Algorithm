import heapq as hq
def solution(operations):
    max_hp,min_hp = [],[]
    nums = []
    for i in range(len(operations)):
        order = operations[i]
        operator,n = order.split()
        if operator == 'I': # insert
            nums.append(int(n))
        else:
            try:
                if n == '-1': #최댓값 삭제
                    hq.heappop(max_hp)
                    nums = max_hp
                elif n == '1':
                    hq.heappop(min_hp)
                    nums = list(map(lambda x: -x,min_hp))
            except:
                pass
        max_hp = nums[:]
        min_hp = list(map(lambda x:-x,nums))
        hq.heapify(max_hp)
        hq.heapify(min_hp)
    if len(nums) != 0:
        return [min_hp[0]*-1,max_hp[0]]
    return [0,0]