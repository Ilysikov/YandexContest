d = int(input())
a = 1
while d != 0:
    n = int(input())
    if d < n:
        d = n
        a = 1
    elif d == n:
        a += 1
    elif n == 0:
        d = 0
        break
print(a)
