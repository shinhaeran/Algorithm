n,m = map(int, input().split())
card = list(map(int, input().split()))
min_diff = 9999999999999
mydeck =[0,0,0]

for i in range(0,n-2):
    # mydeck.append(card[i])
    mydeck[0]=card[i]
    for j in range(i+1,n-1):
        # mydeck.append(card[j])
        mydeck[1]=card[j]
        for k in range(j+1,n):
            # mydeck.append(card[k])
            mydeck[2]=card[k]
            if sum(mydeck) <= m:
                min_diff = min(min_diff, m-sum(mydeck))
            # print(mydeck)
                
print(m-min_diff)


