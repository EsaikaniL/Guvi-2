a=input().strip().split(" ")
max=-1
for x in a:
    if len(x)>max:
        max=len(x)
        k=x
print(k)
