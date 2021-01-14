case = input()
croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
croatia_num = int()
croatia_len = int()

for c in croatia:
    # print(case.split(c))
    num = len(case.split(c))
    if c == 'z=':
        znum = (num-1) #2
        continue
        
    if c == 'dz=':
        if num!= 1:
            znum = znum - (num-1) # 2 -> 1
            croatia_num += num-1 + znum # 1 + 1
            croatia_len += len(c)*(num-1) + len('z=')*znum # -> 3 + 1 = 4
            continue
        else:
            croatia_num += znum #2
            croatia_len += len('z=')*(znum)
            # continue

    if num != 1:
        # num,c = znum,'z='
        croatia_num += num -1 #2
        croatia_len += len(c)*(num-1)

print(len(case)- croatia_len + croatia_num)
