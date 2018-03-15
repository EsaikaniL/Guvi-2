n=int(input())
i=2
ans=""
while(n>0 and i<(n//2)):
    c=0
    for x in range(1,i+1):
        if i%x==0:
            c+=1 
    if c==2:
        if n%i==0:
            ans=ans+str(i)+" "
    i+=1
print(ans.strip())
