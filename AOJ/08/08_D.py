s = input()
p = input()



check = False
for i in range(len(s)):
    if s.count(p) < 1:
        slist = list(s)
        slist += slist[0]
        slist.pop(0)
        s = ''.join(slist)
        continue
    else:
        check = True

if check == True:
    print('Yes')
else:
    print('No')

