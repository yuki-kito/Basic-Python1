n = int(input())
a = list(map(int,input().split()))

while n != 0:
    if n == 1:
        print(a[n-1])
    else:
        print(a[n-1],end = ' ')
    n -= 1