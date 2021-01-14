def select_num(n,lotto,result):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(n+1,len(lotto)):
        temp = result[:]
        if len(lotto)-i >= 6-len(result):
            temp.append(lotto[i])
            select_num(i,lotto,temp)
        else:
            break
input_s = []
while True:
    temp = input().split()
    if temp[0] == '0':
        break
    input_s.append(temp)
for j in range(len(input_s)):
    N = int(input_s[j][0])
    lotto = list(map(int,input_s[j][1:]))
    # print(N,lotto)
    
    for i in range(0,N-6+1):
        select_num(i,lotto,[lotto[i]])
    print()
