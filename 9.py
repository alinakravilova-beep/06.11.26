n, k, r = map(float, input().split())
day = 1
while n < r:
    n += n * k / 100
    day += 1
print(day)