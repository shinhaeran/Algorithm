nums = list()
for i in range(9):
    nums.append(input())
maxN= max(nums)
print(maxN)
print(nums.index(maxN)+1)