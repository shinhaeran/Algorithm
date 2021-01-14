n, pair = map(int,input().split())
deck = [i+1 for i in range(n)]
my_deck = list()
visit = [False] * n
def find_pair(cnt):
    if cnt == pair:
        print(*my_deck)
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i] =  True
        my_deck.append(deck[i])
        find_pair(cnt+1)
        visit[i] = False
        my_deck.pop()
    
find_pair(0)

    




