# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,qn = map(int, input().split())
line = [[False for _ in range(511)] for _ in range(511)]

for _ in range(qn):
    s1,s2,cost = input().split()
    s_binary1 = str()
    for ss in s1:
        if ss == 'o':
            s_binary1 += '1'
        else: #ss == 'x':
            s_binary1 += '0'
    
    s_binary1 = int(s_binary1,2)
    s_binary2 = str()
    for ss in s2:
        if ss == 'o':
            s_binary2 += '1'
        else: #ss == 'x':
            s_binary2 += '0'
    s_binary2 = int(s_binary2,2)
print(line)
	
		