st=input()
ip=list(st)
for x in range(len(ip)-1):
    for y in range(x+1,len(ip)):
        if (ord(ip[x])>ord(ip[y])):
                        t=ip[x]
                        ip[x]=ip[y]
                        ip[y]=t
ans=''
for x in ip:
    ans=ans+x
print(ans)
