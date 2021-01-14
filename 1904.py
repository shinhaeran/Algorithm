n = int(input())
answer = set()
word = str()

def tile01(word):
    
    word_len = len(word)
    if word_len == n:
        answer.add(int(word))
        return
    
    if word_len <= n-2:
        word += '0'
        word += '0'
        tile01(word)
        word = word[:-2]

        word += '1'
        tile01(word)
        # word.pop()
    else: # 한 칸 남았을 때
        word += '1'
        tile01(word)
tile01('')
print(len(answer)%15746)