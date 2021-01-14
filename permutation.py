# from itertools import permutations
# l1 = [i+1 for i in range(5)]
# permutation_li = permutations(l1,len(l1))
arr = [i+1 for i in range(5)]
result = [arr[:]]
c = [0] * len(arr)
i = 0

while i < len(arr):
    if c[i] < i:
        if i % 2 == 0:
            arr[0], arr[i] = arr[i],arr[0] # swap
        else:
            arr[c[i]], arr[i] = arr[i], arr[c[i]]
        result.append(arr[:])
        c[i] += 1
        i =0
    else:
        c[i] =0
        i += 1
    print(c,i,arr)
    
    
    # print(arr,c[i])
# print(len(result), len(set(result)))

    
    