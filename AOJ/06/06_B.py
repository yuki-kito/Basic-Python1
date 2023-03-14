n = int(input())
group = []
while n != 0:
    a,b1 = input().split()
    b = int(b1)
    group += [(a,b)]
    n -= 1

scount = list(range(1,14))
hcount = list(range(1,14))
ccount = list(range(1,14))
dcount = list(range(1,14))
for (picture,figure) in group:
    if picture == 'S':
        scount.remove(figure)
    elif picture == 'H':
        hcount.remove(figure)
    elif picture == 'C':
        ccount.remove(figure)
    elif picture == 'D':
        dcount.remove(figure)

for i in scount:
    print('S ' + str(i))
for j in hcount:
    print('H ' + str(j))
for t in ccount:
    print('C ' + str(t))
for k in dcount:
    print('D ' + str(k))
