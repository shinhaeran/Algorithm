def solution(N, number):
    if N == number:
        return 1
    set_list = [0] + [set() for _ in range(8)]
    temp = str(N)
    set_list[1].add(int(temp))

    for i in range(2,9):
        temp += str(N)
        set_list[i].add(int(temp))
        for j in range(1,i): # set_list[j] | set_list[i-j]
             for n1 in set_list[j]:
                    for n2 in set_list[i-j]:
                        set_list[i].add(n1+n2)
                        set_list[i].add(n1-n2)
                        set_list[i].add(n1*n2)
                        if n2 != 0:
                            set_list[i].add(int(n1/n2))
        if number in set_list[i]:
            # print(set_list)
            return i    

    return -1