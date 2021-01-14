n = int(input())
count = 1
if n == count:
    print('666')
else:
    for i in range(1666,10000000):
        if '666' in str(i):
            count +=1
        if count == n:
            print(i)
            break   