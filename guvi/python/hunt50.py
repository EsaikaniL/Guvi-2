st=input().strip()
n=int(st.split(" ")[0])
k=int(st.split(" ")[1])
x=0
while(n>=k):
    n-=k
    x+=1
print(x)
