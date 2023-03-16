array = []

while True:
    x = input()
    if x == '0':
        break
    array.append(x)

for i in array:
    sum = 0
    for j in list(i):
        sum += int(j)
    print(sum) 