x = int(input())
second = x % 60
minute = (x // 60) % 60
hour = x // 3600
print(str(hour) + ':' + str(minute) + ':' + str(second))