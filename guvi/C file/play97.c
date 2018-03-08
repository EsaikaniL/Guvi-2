#include <stdio.h>

int main()
{
   int l,n,i,ans=0;
   scanf("%d",&l);
   scanf("%d",&n);
   for(i=l;i<=n;i++)
   {
       if(i%2==1)
       {
           ans=ans+i;
       }
   }
   printf("%d",ans);
    return 0;
}
