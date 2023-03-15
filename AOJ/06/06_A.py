n = int(input())
a = list(map(int,input().split()))
x = 1
a.reverse()

for i in a:
    if x == n:
        print(i)
    else:
        print(i,end=' ')
    x += 1