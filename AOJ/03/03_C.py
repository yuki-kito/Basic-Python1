a = []
while True:    
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    else:
        a += [ (x,y) ]

y = 0
while True:    
    if y == len(a):
        break
    else:
        if a[y][0] < a[y][1]:
            print(str(a[y][0]) + ' ' + str(a[y][1]))
            y += 1    
        else:
            print(str(a[y][1]) + ' ' + str(a[y][0]))
            y += 1

    
