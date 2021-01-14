ploblem = input().upper()
alphabet_set = set(ploblem)
alphabet_dict = dict()

for s in alphabet_set:
    alphabet_dict[s] = ploblem.count(s) # alphabet : frequency

temp = list(alphabet_dict.values())
max_frequency = max(temp)
if temp.count(max_frequency) != 1:
    print('?')
else:
    for k,v in alphabet_dict.items():
        if v == max_frequency:
            print(k)
            break
# 굳이 dict로 안하고 그냥 set -> list로 맹글고 이에 상응하는 frequency list도 하나 만들어서 인덱스로 접근해도 된다 !
# a=input()
# a=a.upper()
# c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# b=[]
# for i in range(len(c)):
#     k=a.count(c[i])
#     b.append(k)
# if b.count(max(b))>1:
#     print('?')
# else:
#     print(c[b.index(max(b))])