def fac(num):
    ans=1
    for x in range(1,num+1):
        ans*=x
    return ans
n=int(input())
print(str(fac(2*n)//(fac(n)*fac(n+1))))
