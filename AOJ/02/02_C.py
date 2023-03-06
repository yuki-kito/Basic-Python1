x = list(map(int,input().split()))
for j in range(2):
    for i in range(1 , 3 - j ):
        if x[ j + i ] < x[ j ]:
            y = x[:]
            x[ j ] = y[ j  +  i ]
            x[ j + i ] = y[ j ]

for a,b in enumerate(x,1):
    if a == 3:
        print(b)
    else:
        print(b, end=' ')