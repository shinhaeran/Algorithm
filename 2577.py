result = int(input())
for i in range(2):
    result *= int(input())
result = str(result)
result_list = list(result)

for i in range(10):
    print(result_list.count(str(i)))