n=int(input().strip())
ip=input().strip().split(" ")
a=[]
b=[]
ma=-100000
mi=100000
i=0
j=0
for x in range(n):
    for y in range(n):
        if x!=y:
            if int(ip[x])+int(ip[y])<0:
                m=int(ip[x])+int(ip[y])
                a.append(m)
                a.append(ip[x]+" "+ip[y])
            elif int(ip[x])+int(ip[y])>=0:
                m=int(ip[x])+int(ip[y])
                b.append(m)
                b.append(ip[x]+" "+ip[y])
for x in range(0,len(a),2):
    if a[x]>=ma:
        ma=a[x]
for x in range(0,len(b),2):
    if b[x]<=mi:
        mi=b[x]
for x in range(ma,0):
    i+=1
for x in range(mi):
    j+=1
if min(i,j)==i:
    print((a[a.index(ma)+1]).strip())
else:
    print((b[b.index(mi)+1]).strip())
