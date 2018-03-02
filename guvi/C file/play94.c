#include <stdio.h>
int main()
{
int n,i,t,a[255],flag=0,k=0;
scanf("%d",&n);
while(n>0)
{
    t=n%10;
    a[k]=t;
    for(i=0;i<k;i++)
    {
       if(a[i]==t)
       {
           flag=1;
           break;
       }
    }
    k++;
    n=n/10;
}
if(flag==0){printf("\nYes");}
else { printf("\nNo");}
}
