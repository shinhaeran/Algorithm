answer = list()
def hanoi(s,d,t,n):#sorce, destination,temp, n:현재 덩어리 몇개?
    global answer
    if n ==1: #찐 이동
        answer.append((s,d))
        return 
    #n-1까지 t로 이동
    hanoi(s,t,d,n-1)
    #n층을 d로
    hanoi(s,d,t,1)
    #t에 있는 n-1층들을 d로
    hanoi(t,d,s,n-1)

n = int(input()) # 원판의 갯수
# arr = [[] for _ in range(3)]
hanoi(1,3,2,n)

print(len(answer))
for s,d in answer:
    print(s,d)