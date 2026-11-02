p = float(input())
k = 0
if p != 0:
    while True:
        t = float(input())
        if t == 0:
            break
        if t < p:
            k += 1
        p = t
print(k)