import random


def week():
    return ' '.join(map(str, [random.randrange(3), random.randrange(3), random.randrange(3)]))


x, y, c = 0, 0, 0
tab = []
dic = {}
res = "NO"
for i in (0, 3, 6):
    npu = input()
    x += npu.count("1") if "1" else 0
    y += npu.count("2") if "2" else 0
    c += npu.count("0") if "0" else 0
    lit = list(map(int, npu.split()))
    dic[1 + i], dic[2 + i], dic[3 + i] = lit[0] + 1, lit[1] + 1, lit[2] + 1
if x >= 3 and (x == y or x - 1 == y):
    exe = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    col = []
    for z in exe:
        s = set()
        for n in z:
            if dic[n]:
                s.add(dic[n])
        if (s == {2} or s == {3}) and s not in col:
            col.append(s)
    if len(col) == 1:
        if (col[0] == {2} and x - 1 == y) or (col[0] == {3} and x == y):
            res = "YES"
        else:
            res = "NO"
    elif len(col) >= 2:
        res = "NO"
    elif not col:
        res="YES"
elif x < 3 and (x == y or x - 1 == y):
    res = "YES"
elif x >= 3 and not (x == y or x - 1 == y):
    res = "NO"
print(res)