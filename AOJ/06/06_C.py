n = int(input())
check = [[[0 for i in range(10)]  for j in range(3)] for k in range(4) ] 
x = 0 

while n != 0:
    b,f,r,v = map(int,input().split())
    check[b - 1][f - 1][r - 1] += v
    n -= 1
    

for building in check:
    for floor in building:
        for round in floor:
            print(' ',end='')
            print(round,end='')    
        print()
    if x != 3:
        print('#' * 20)
    x += 1
    