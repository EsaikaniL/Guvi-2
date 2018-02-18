st=input("Enter your number:")
p=st[::-1]
c=0
if p[0]=='0':
    for x in p:
        if x=='0':
            c+=-(-1)
        else:
            break
k=c*'0'+st
if int(st)==int(k):
    print("yes")
else:
    print("No")
