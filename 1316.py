num = int(input())
group_word = num
for n in range(num):
    case = input()
    case_set = set(case)
    prev = case[0]
    case_set.remove(prev)
    for s in case[1:]:
        if prev ==s:
            continue
        else:
            try:
                case_set.remove(s)
            except Exception:
                group_word -= 1
                break
        prev = s
print(group_word)