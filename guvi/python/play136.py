st=input().strip().split(" ")
n=int(st[0])
k=int(st[1])
st=input().strip().split(" ")
a=[]
c=0
for x in range(n):
    a.append(int(st[x]))
for x in a:
    if x==k:
        c+=1
if c==0:
    print("no")
else:
    print("yes"+" "+str(c))
