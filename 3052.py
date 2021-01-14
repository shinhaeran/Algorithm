#내꺼
a = dict()
for i in range(10):
    a[int(input())%42] = i
print(len(a))