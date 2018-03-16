n=int(input())
a=input().strip().split(" ")
ans=1
for x in a:
    ans*=int(x)
if ans%2==0:
    print("even")
else:
    print("odd")
