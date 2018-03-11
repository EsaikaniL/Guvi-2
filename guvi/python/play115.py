st=input()
a=list(st.split(" ")[0])
b=list(st.split(" ")[1])
if len(a)!=len(b):
    if max(len(a),len(b))==len(a):
        for x in range(len(a)-len(b)):
            a.pop()
    else:
        for x in range(len(b)-len(a)):
            b.pop()
ans=""
for x in a:
    ans+=x
for x in b:
    ans+=x
print(ans)
