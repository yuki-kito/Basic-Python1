n = int(input())
group = []
group = [(input().split()) for i in range(n)]

scount = list(range(1,14))
hcount = list(range(1,14))
ccount = list(range(1,14))
dcount = list(range(1,14))
for (picture,figure1) in group:
    figure = int(figure1)
    if picture == 'S':
        scount.remove(figure)
    elif picture == 'H':
        hcount.remove(figure)
    elif picture == 'C':
        ccount.remove(figure)
    elif picture == 'D':
        dcount.remove(figure)

for i in scount:
    print('S',i)
for j in hcount:
    print('H',j)
for t in ccount:
    print('C',t)
for k in dcount:
    print('D',k)
