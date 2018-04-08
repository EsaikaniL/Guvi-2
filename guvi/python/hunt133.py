ip=input().strip().split(" ")
ans=""
for x in range(len(ip),0,-1):
    ans+=ip[x-1]+" "
print(ans.strip())
