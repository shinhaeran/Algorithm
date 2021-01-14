def find_self_num(generator_list,num):
    # 2-> 1+1 4-> 4+4 ; selfNum만 출력 | 10000이하
    # 10000 이하 수에서 생성자 다 구한다음에 빼야하나? -> 문제 보니께 재귀로 풀어야 할거같은딩
    if num > 10000:
        return generator_list
    else:
        num_sum = num
        num = str(num)
        
        for s in num:
            num_sum += int(s)

        num_sum = int(num_sum)
        if num_sum in generator_list: #바로 빠져나와야함
            return generator_list
        else:
            generator_list.append(num_sum)

generator_list = list()
for i in range(1,10001):
    find_self_num(generator_list,i)

for i in range(1,10001):
    if not i in generator_list:
        print(i)

        
