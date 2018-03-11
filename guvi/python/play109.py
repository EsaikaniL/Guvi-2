n=int(input())
k=input().strip()
a=k.split(" ")
ans=""
p=0
a.sort()
for x in a:
    p+=int(x)
for x in a[::-1]:
    ans=ans+str(p)+" "
    p-=int(x)
print(ans.strip())
