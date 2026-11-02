x = int(input())
s = 0
a = ""
for i in range(1, x + 1):
    s += i
    if i == 1:
        a = str(i)
        print(a)
    else:
        a += " + " + str(i)
        print(a, "=", s)