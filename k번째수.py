def solution(array, commands):
    answer = []
    for command in commands:
        start,end,ans = command
        # print(type(sorted(array[start-1:end])))
        answer.append(sorted(array[start-1:end])[ans-1])
    return answer