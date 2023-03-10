a,b,c = map(int,input().split())
figure = 0
for i in range(a, b + 1):
    if c % i == 0:
        figure += 1

print(figure)