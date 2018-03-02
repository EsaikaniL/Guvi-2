#include <stdio.h>

int main()
{
    int n,t,flag=0,ans;
    scanf("%d",&n);
    while(n>0)
    {
        t=n%10;
        if(flag==0)
        {
            ans=t;
        }
        n=n/10;
        flag=1;
    }
    printf("\n%d",ans+t);
}
