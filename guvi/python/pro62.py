st=input("Enter your string:")
s=list(st)
l=-1
for x in range(len(s)):
    for y in range(x+1,len(s)+1):
        ans=''
        for z in range(x,y):
            ans=ans+s[z]
        if ans==ans[::-1]:
            if len(ans)>l:
                l=len(ans)
print("Answer:",len(st)-l)
