st=input("Enter your string")
a=0
ans=[]
l=len(st)
for x in range(0,l-1):
    if st[x]=='a' and st[x+1]=='b':
        a=a+2
    elif st[x]!='a' and st[x]!='b':
        ans.append(a)
        a=0
    elif (st[x]=='b' and st[x+1]=='b') or (st[x]=='a' and st[x+1]=='a'):
    	ans.append(a)
    	a=0
ans.append(a)
print(max(ans))
