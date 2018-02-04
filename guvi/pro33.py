def myfun(l,t):
    p=1
    for x in range(1,t+1):
        p=p*x
    return(l*p)

st=input("Enter the string:")
a=[]
for x in range(len(st)):
    for y in range(x+1,len(st)):
        ans=''
        for z in range(x,y+1):
            ans+=st[z]
        a.append(ans)
max=-1
for x in a:
    ans=0
    for i in range(len(x)):
        tmp=0
        l=0
        for j in range(i+1,len(x)):
            l+=1
            if ord(x[i])>ord(x[j]):
                tmp+=1
        ans+=myfun(tmp,l)
        if max<ans:
            max=ans
            k=x
print(k)
            
    
