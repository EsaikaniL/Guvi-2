st1=input("Enter Your name:").lower().strip()
st2=input("Enter your partner name:").lower().strip()
a=list(st1)
b=list(st2)
k1=0
k2=0
for x in range(len(a)):
               for y in range(len(b)):
                   if a[x]==b[y]:
                       a[x]='*'
                       b[y]='*'
                       break
for x in a:
    if x!='*':
        k1+=1
for x in b:
    if x!='*':
        k2+=1
f=['f','l','a','m','e','s']
f1=[]
flag=0
i=0
for x in range(5):
    n=1
    i=0
    if flag==1:
        f=f1
        f1=[]
        
    while(n<=k1+k2):
        flag=1
        if i>=len(f)-1:
            i=0
        else:
            i+=1
        n+=1
        
        if n==(k1+k2):
            for y in range(i+1,len(f)):
                f1.append(f[y])
            for y in range(0,i):
                f1.append(f[y])
for x in f1:
    if x=='f':
        print("You are Friends!!!")
    if x=='l':
        print("You are Lovers!!!")
    if x=='a':
        print("You have Attraction on your partner!!!")
    if x=='m':
        print("You are going to Marry your partner!!!")
    if x=='e':
        print("You are Enemes!!!")
    if x=='s':
        print("Your partner is Brother (or) Sister!!!")
