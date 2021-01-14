n = int(input())

for i in range(n):
    test_num, test_str = input().split(' ')
    
    ans = str()
    for s in test_str: 
        ans += int(test_num) * s
    print(ans)

    