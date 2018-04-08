ip=input().strip().split(" ")
n=int(ip[0])
m=int(ip[1])
c=0
for x in range(2,min(n,m)+1):
    if n%x==0 and m%x==0:
        c+=1
if c==0:
    print("yes")
else:
    print("no")
