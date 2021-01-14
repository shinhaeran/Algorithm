days = int(input())
task = []
for _ in range(days):
    t,p = map(int,input().split())
    task.append((t,p))
    # print(t,p)
print(task)