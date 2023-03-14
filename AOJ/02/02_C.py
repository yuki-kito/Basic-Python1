x = list(map(int,input().split()))
x.sort()

for a,b in enumerate(x,1):
    if a == 3:
        print(b)
    else:
        print(b,end=' ')