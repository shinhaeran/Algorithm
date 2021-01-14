n = int(input())
person = list()
for _ in range(n):
    person.append(tuple((map(int,input().split()))))

result = list()

for i in range(n):
    count = 0
    for j in range(n):
        if i == j :
            continue
        # print(person[i],person[j])
        if person[i][0]<person[j][0] and person[i][1]<person[j][1]:
            count += 1
    result.append(count+1)

for score in result:
    print(score, end=' ')
