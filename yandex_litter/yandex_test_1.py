h = "once upon a time, in a , land far ,far away lived a n,o,p,yande princess , whose beauty was yet , 333,unmatched, rr, , eeee,, aa "
h = h * 10 ** 5
st = h  # input()
st_l = []
b = ""
g = 0
for a in st:
    if a == "," and b:
        g = len(b) if len(b) > g else g
        b += a
        st_l.append(b)
        b = ""
    elif a == " " and b:
        g = len(b) if len(b) > g else g
        st_l.append(b)
        b = ""
    elif a == "," and not b:
        st_l[-1] += a
    elif a != " " and a != ",":
        b += a
if b:
    g = len(b) if len(b) > g else g
    st_l.append(b)
    b = ""
l = g * 3
en = []
le = 0
mys = ''
an = []
for i in st_l:
    if le + len(i) + len(en) <= l:
        en.append(i)
        le += len(i)
    elif le + len(i) + len(en) > l:
        mys = ' '.join(en)
        an.append(mys)
        en = []
        mys = ''
        le = len(en)
        en.append(i)
        le += len(i)
if en:
    mys = ' '.join(en)
    an.append(mys)
    en = []
    mys = ''
with open('output.txt', 'a') as file:
    for a in an:
        file.write(a)
        file.write("\n")
