st=input()
a=[]
b=[]
ans=""
i=0
for x in st:
    if x.isalpha():
        a.append(x)
    elif x.isdigit():
        b.append(int(x))
for x in b:
    ans+=x*a[i]
    i+=1
print(ans.strip())
