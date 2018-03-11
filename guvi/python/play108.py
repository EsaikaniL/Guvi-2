n=int(input())
k=input().strip()
a=k.split(" ")
ans=""
p=0
for x in a:
    p=p+int(x)
    ans=ans+str(p)+" "
print(ans.strip())
    
