a,b = map(int,input().split())
d = a // b
r = a % b
f = a / b

print(f"{d} {r} {format(f,'.10f')}")