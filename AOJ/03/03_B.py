a = []
while True:    
    x = int(input())
    if x == 0:
        break
    else:
        a += [x]

y = 0
while True:    
    if y == len(a):
        break
    else:
        print('Case ' + str(y + 1) + ': ' + str( a[y]))
        y += 1    
    