array = []

while True:
    n,x = map(int, input().split())
    if n == 0 and x == 0:
        break
    array += [(n,x)]

for (n1,x1) in array:
    count = 0
    for i in range(1,n1 - 1) :
        for j in range(i + 1, n1):
            if (j < ((x1 - i) - j)) and (((x1 - i) - j) <= n1):
                count += 1         
    print(count)