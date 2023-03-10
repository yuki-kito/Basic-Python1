import math
r = float(input())

area = r * r * math.pi
length = 2 * r * math.pi

print(f"{format(area,'.6f')} {format(length,'.6f')}")