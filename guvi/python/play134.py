st=input().strip().split(" ")
n=int(st[0])
l=int(st[1])
r=int(st[2])
a=[]
st=input().strip().split(" ")
for x in range(n):
    a.append(int(st[x]))
mi=10000000
for x in range(l-1,r):
    if a[x]<mi:
        mi=a[x]
print(mi)
