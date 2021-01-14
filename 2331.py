n = int(input())
gen = str()
gen_min = 999999999999
for i in range(1,n+1):
    gen = str(i)
    gen_sum = i
    for k in map(int,gen):
        gen_sum += k
    if gen_sum == n :
        gen_min = min(gen_min,i)
        
if gen_min == 999999999999:
    print(0)
else:
    print(gen_min)

