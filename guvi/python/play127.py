s1=input().strip().split(" ")
s2=input()
ans=""
for x in s1:
    if x!=s2:
        ans+=x+' '
print(ans.strip())
