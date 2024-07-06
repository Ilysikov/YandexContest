a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==0 and b==0:
    res="INF"
elif a==0 and b!=0:
    res=("NO")
elif b%a==0 and c*-(b/a)!=-d:
    res=-(b//a)
else:
    res="NO"
print(res)