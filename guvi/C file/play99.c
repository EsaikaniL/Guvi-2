#include <stdio.h>
int main()
{
    int n,t,i=0,j=0,temp=0,ans=0,a[3]={1,2,4};
    scanf("%d",&n);
    while(n>0)
    {
        t=n%10;
        temp=temp+(t*a[i++]);
        if(i==3)
        {
            ans=ans*10+temp;
            i=0;temp=0;
        }
        n=n/10;
    }
     printf("\n%d",ans);
    return 0;
}
