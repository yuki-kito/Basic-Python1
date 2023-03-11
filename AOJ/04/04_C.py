while True:
    a,op,b = input().split()
    a1 = int(a)
    b1 = int(b)
    if op == '+':
        print(a1 + b1)
    elif op == '-':
        print(a1 - b1)
    elif op == '*':
        print(a1 * b1)
    elif op == '/' :
        print(a1 // b1)
    elif op == '?':
        break