best = 0
while True:
    x = int(input())
    if x == -1:
        break
    if x > best:
        best = x
print(best)