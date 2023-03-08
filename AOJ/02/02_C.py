x = list(map(int,input().split()))

for a,b in enumerate(sorted(x),1):
    if a == 3:
        print(b)
    else:
        print(b,end=' ')