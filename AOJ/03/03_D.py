a,b,c = map(int,input().split())
figure = 0
for i in range(b - a + 1):
    if c % (i + a) == 0:
        figure += 1

print(figure)