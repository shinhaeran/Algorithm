s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = str()
for a in alphabet:
    try:
        ans = s.index(a)
        
    except ValueError:
        ans = '-1'
    
    print(ans,end=' ')



