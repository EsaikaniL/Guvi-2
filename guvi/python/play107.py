st=input().strip()
a=st.split(" ")
k=input()
for x in range(len(a)):
    if k==a[x]:
        print(x+1)
