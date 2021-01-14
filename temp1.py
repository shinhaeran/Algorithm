# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
win_score = dict() #win[0] : a팀의 승리 횟수
set_score = dict() #set_socre[0] : a팀의 세트 득실
for _ in range(n*(n-1)):
    t1, s1, t2, s2 = input().split()
    s1,s2 = int(s1),int(s2)
    try:
        set_score[t1] += 0
    except:
        set_score[t1] = 0
        win_score[t1] = 0
    try:
        set_score[t2] += 0
    except:
        set_score[t2] = 0
        win_score[t2] = 0

    if s1 > s2: # t1이 이김
        win_score[t1] += 1
        set_score[t1] += s1 -s2
        set_score[t2] += s2 - s1
    
    else: #t2가 이김
        win_score[t2] += 1
        set_score[t1] += s1 -s2
        set_score[t2] += s2 - s1

soreted_score = sorted(win_score.items(),key = (lambda x: x[1]))

#승리횟수 같은 팀 찾기
score = [[] for _ in range(n*(n-1))]
for t,s in soreted_score:
    score[s].append(t)
# print(score)

for s in score[::-1]:
    if len(s) > 1:
        s.sort()
        for ss in s:
            print(ss,win_score[ss],set_score[ss])
    elif len(s)==1:
        print(s[0],win_score[s[0]],set_score[s[0]])
    
