case = input()
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# convert = list()
answer = int()
for s in case:
    # convert.append(int(alphabet.index(s)/3)+2)
    if s in 'ABC':
        answer += 2 +1
    elif s in 'DEF':
        answer += 3 +1
    elif s in 'GHI':
        answer += 4 +1
    elif s in 'JKL':
        answer += 5 +1
    elif s in 'MNO':
        answer += 6 +1
    elif s in 'PQRS':
        answer += 7 +1
    elif s in 'TUV':
        answer += 8 +1
    elif s in 'WXYZ':
        answer += 9 +1

print(answer)

# A -> 2 ->3
# B -> 2 ->3