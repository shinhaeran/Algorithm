def solution(begin, target, words):
    answer = 0
    from collections import deque
    q = deque()
    q.appendleft(begin)
    n = len(begin)
    while q:
        word = q.pop()
        if word == target:
            break
        temp = deque()
        for j in range(len(words)-1,-1,-1):
            cnt = 0
            for i in range(n):
                if words[j][i] != word[i]:
                    cnt += 1
            if cnt == 1:
                temp.appendleft(words.pop(j))
        answer += 1
        q = temp
    if word != target:
        answer = 0
    
    return answer