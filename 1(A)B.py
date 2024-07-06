dic = {}
d=int(input())
for o in range(d):
    dic[o] = list(map(int, input().split()))
for i in range(d):
    res = "NO"
    tup=[]
    for x,y in zip(dic[i][::2],dic[i][1::2]):
        tup.append((x,y))
    tup.sort()
    if tup[1][0] - tup[0][0] == tup[3][0] - tup[2][0] and tup[1][1] - tup[0][1] == tup[3][1] - tup[2][1]:
        res = "YES"
    dic[i]=res
for k in range(d):
    print(dic[k])