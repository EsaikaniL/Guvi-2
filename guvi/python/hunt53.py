st=input().strip().split(" ")
s=list(st[0])
k=int(st[1])
ans1=""
for x in range(0,len(s)-k+1):
    ans=""
    for y in range(x,x+k):
        ans+=str(s[y])
    ans1+=ans+" "
print(ans1.strip())
