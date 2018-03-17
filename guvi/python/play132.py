n=input().strip()
c=0
if int(n[0])%2==0:
    f1=1
    for x in n:
        if  f1==1 and int(x)%2==0:
            f1=0
            c+=1
        if f1==0 and int(x)%2!=0:
            f1=1
            c+=1
else:
    f1=1
    for x in n:
        if  f1==1 and int(x)%2!=0:
            f1=0
            c+=1
        if f1==0 and int(x)%2==0:
            f1=1
            c+=1
print(c)
