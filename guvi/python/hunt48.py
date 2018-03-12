s1=list(input().strip())
s2=input()
k=-1
for x in range(len(s1)):
    for y in range(x+1,len(s1)):
        ans=""
        for z in range(x,y+1):
            ans+=s1[z]
        if ans==s2:
            k=x
    if k!=-1:
        break
print(k)
