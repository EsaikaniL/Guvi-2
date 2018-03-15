n=int(input())
a=input().strip().split(" ")
for x in range(1,10000):
    c=0
    for y in a:
        if x%int(y)==0:
            c=1
        else:
            c=0 
            break
    if c==1:
        break
print(x)
