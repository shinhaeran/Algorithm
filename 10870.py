# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def cal(arr,group,min_cost,index,k,n):
	# print(group, index)
	
	cost = int()
	total = int()
	if index == n: #cost 계산
		for p in group:
			if len(p) > 1:
				total += max(p)-min(p)
				# print('total',total, type(total),group, index)
		return total
	
	for i in arr[index:]:
		for j in range(k):
			copy_group = group[:]
			copy_group[j].append(i)
			cost = cal(arr, copy_group, min_cost, index+1, k, n)
			# print(type(min_cost), type(cost), group, index)
			if min_cost > int(cost):
				min_cost = cost
	return min_cost

n,k = map(int,input().split())

arr = list(map(int,input().split()))

group = list()
for _ in range(k):
	group.append(list())

cost = cal(arr, group, 999999999, 0 ,k,n)
print(cost)

	
	