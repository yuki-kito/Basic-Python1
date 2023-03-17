array =[]
alphabets = [0 for i in range(26)]
while True:
    try:
        x = input()
    except:
        break
    y = x.lower()
    array.append(y)

for y in array:
    for i in list(y):
        for j in range(26):
            if ord(i)== (97 + j) :
                alphabets[j] += 1

for i in range(26):
    print(chr(97 + i),':',alphabets[i])
