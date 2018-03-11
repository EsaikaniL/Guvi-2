st=list(input())[::-1]
ans=""
for x in range(len(st)):
    if x!=len(st)-1:
        ans+=str(st[x])+"-"
    else:
        ans+=str(st[x])
print(ans)
