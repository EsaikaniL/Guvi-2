st=input().strip().split(" ")
n=int(st[0])
m=int(st[1])
a=[]
f=0
for x in range(n):
    k=input().strip().split(" ")
    a.append(int(k[0]))
    a.append(int(k[1]))
for x in a:
    if m<=x:
        f=1
        break 
if f==1:
    print("yes")
else:
    print("no")
