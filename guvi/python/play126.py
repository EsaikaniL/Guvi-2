st=input().strip().split(" ")
n=int(st[0])
k=int(st[1])
a=input().strip().split(" ")
a.sort()
ans=""
b=[0]*256
for x in a:
    b[ord(x)]+=1
for x in a:
    if b[ord(x)]<k and x not in ans:
        ans+=x+' '
print(ans.strip())
