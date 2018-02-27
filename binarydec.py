num=input('Enter the number \n')
flag=0
for x in num:
    if int(x)!=0 and int(x)!=1:
        flag=1
        break
if  flag==1:
    print("No")
else:
    print("Yes")
