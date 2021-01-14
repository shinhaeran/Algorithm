def draw_star(x,y,size,arr):
    # global arr
    if size == 1:
        return arr

    # size > 3, 27->9->3 ..
    flag = int()
    for yy in range(0,size,int(size/3)):
        for xx in range(0,size,int(size/3)):
            # print(size,x,y,xx,yy,flag)
            if not flag == 4:
                if size == 3:
                    arr[y+yy][x+xx] = '*'
                else:
                    draw_star(x+xx,y+yy,int(size/3),arr)
            flag += 1

n = int(input())
arr = [ [' ' for _ in range(n)] for _ in range(n)]
draw_star(0,0,n,arr)

for e in arr:
     print(*e, sep='')
