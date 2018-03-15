st=input().strip()
a=[]
b=['a','e','i','o','u','A','E','I','O','U']
for x in st:
    if x in b:
        a.append(x)
for x in st:
    if x not in a:
        a.append(x)
ans=""
for x in a:
    ans+=x
print(ans.strip())
